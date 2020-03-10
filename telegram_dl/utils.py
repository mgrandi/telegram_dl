import attr
import json
import pathlib
import logging
import typing
import signal
import uuid
import decimal
import argparse
import base64

import cattr
import arrow
import pyhocon

from telegram_dl import tdlib_generated
from telegram_dl import constants


from sqlalchemy.engine.url import URL

logger = logging.getLogger(__name__)

converter_logger = logger.getChild("converter")
structure_logger = converter_logger.getChild("structure")
unstructure_logger = converter_logger.getChild("unstructure")



class AllowEverythingButThisLoggerFilter:
    ''' logging filter that allows everything but the string specified
    '''

    def __init__(self, dont_allow_this):
        self.dont_allow_this = dont_allow_this

    def filter(self, record):
        '''
        Is the specified record to be logged? Returns zero for no, nonzero for yes.
        If deemed appropriate, the record may be modified in-place by this method
        '''

        if self.dont_allow_this in record.name:
            return 0
        else:
            return 1

def fix_phone_number(phone_number:str) -> str:
    ''' add a plus infront of the phone number if it
    doesn't have one so `phonenumbers` can parse it
    '''
    if not phone_number.startswith("+"):
        return f"+{phone_number}"
    else:
        return phone_number

def get_sqlalchemy_url_from_hocon_config(config:pyhocon.ConfigTree) -> URL:

    driver = config.get_string(constants.CONFIG_KEY_DATABASE_DRIVER)
    user = config.get_string(constants.CONFIG_KEY_DATABASE_USER)
    password = config.get_string(constants.CONFIG_KEY_DATABASE_PASSWORD)
    host = config.get_string(constants.CONFIG_KEY_DATABASE_HOST)
    port = config.get_string(constants.CONFIG_KEY_DATABASE_PORT)
    db = config.get_string(constants.CONFIG_KEY_DATABASE_DATABASE)
    query = config.get_string(constants.CONFIG_KEY_DATABASE_QUERY)


    return URL(drivername=driver,
        username=user,
        password=password,
        host=host,
        port=port,
        database=db,
        query=query)



def register_custom_types_with_cattr_converter(cattr_converter):
    '''
    register custom type hooks with our cattr converter

    TODO: get rid of cattrs or incorporate this into the cattr custom subclass
    '''


    # decimal
    cattr_converter.register_unstructure_hook(decimal.Decimal, lambda x: str(x))
    cattr_converter.register_structure_hook(decimal.Decimal, lambda inst, cl: decimal.Decimal(inst))

    # bytes are already registered by default with `cattr` but in this case, tdjson is
    # giving us a base64 string so we need to override the default converter methods do some additional logic
    # or else we get errors such as `TypeError: string argument without an encoding` when calling `bytes()`
    # with a string
    #
    # NOTE: this might change depending on how we convert the class to JSON in the future, we might want to leave
    # the data as bytes in the JSON (when we are unstructuring) and then a JSONEncoder could convert bytes -> base64,
    # or when structuring from JSON, a JSONDecoder could convert base64 into bytes for us, and therefore the cattr
    # converter won't need these handlers anymore

    def _structure_bytes(bytes_to_structure, klass):

        # we get base64 back from tdjson
        if isinstance(bytes_to_structure, str):
            return base64.b64decode(bytes_to_structure)
        else:
            # if they are already bytes, just pass them through
            return bytes_to_structure


    def _unstructure_bytes(bytes_to_structure):

        # base64 encode it for tdjson
        return base64.b64encode(bytes_to_structure)

    # bytes
    cattr_converter.register_unstructure_hook(bytes, _unstructure_bytes)
    cattr_converter.register_structure_hook(bytes, _structure_bytes)

def new_extra():
    return str(uuid.uuid4())

class ArrowLoggingFormatter(logging.Formatter):
    ''' logging.Formatter subclass that uses arrow, that formats the timestamp
    to the local timezone (but its in ISO format)
    '''

    def formatTime(self, record, datefmt=None):
        # use the 'timestamp' format code
        return arrow.get(f"{record.created}", "X").to("local").isoformat()

def hocon_config_file_type(stringArg):
    ''' argparse type method that returns a pyhocon Config object
    or raises an argparse.ArgumentTypeError if this file doesn't exist

    @param stringArg - the argument given to us by argparse
    @return a dict like object containing the configuration or raises ArgumentTypeError
    '''

    resolved_path = pathlib.Path(stringArg).expanduser().resolve()
    if not resolved_path.exists:
        raise argparse.ArgumentTypeError("The path {} doesn't exist!".format(resolved_path))

    conf = None
    try:
        conf = pyhocon.ConfigFactory.parse_file(str(resolved_path))
    except Exception as e:
        raise argparse.ArgumentTypeError(
            "Failed to parse the file `{}` as a HOCON file due to an exception: `{}`".format(resolved_path, e))

    return conf

def isFileType(filePath):
    ''' see if the file path given to us by argparse is a file
    @param filePath - the filepath we get from argparse
    @return the filepath as a pathlib.Path() if it is a file, else we raise a ArgumentTypeError'''

    path_maybe = pathlib.Path(filePath)
    path_resolved = None

    # try and resolve the path
    try:
        path_resolved = path_maybe.expanduser().resolve(strict=True)

    except Exception as e:
        raise argparse.ArgumentTypeError("Failed to parse `{}` as a path: `{}`".format(filePath, e))

    # double check to see if its a file
    if not path_resolved.is_file():
        raise argparse.ArgumentTypeError("The path `{}` is not a file!".format(path_resolved))

    return path_resolved

def register_ctrl_c_signal_handler(func_to_run):

    def inner_ctrl_c_signal_handler(sig, frame):

        logger.info("SIGINT caught!")
        func_to_run()

    signal.signal(signal.SIGINT, inner_ctrl_c_signal_handler)



class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, pathlib.Path):
            return str(obj)
        elif isinstance(obj, uuid.UUID):
            return str(obj)

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

class CustomCattrConverter(cattr.Converter):
    '''
    subclass of cattr.Converter so we can overwrite a method to make it so that
    we include the @type entries in the dict

    these were taken from the cattrs source code,` cattrs/src/cattr/converters.py `
    git revision 0460fbe825a1e7e50919c5d80e412a309dd96c54
    https://github.com/Tinche/cattrs/blob/0460fbe825a1e7e50919c5d80e412a309dd96c54/src/cattr/converters.py

    '''

    def __init__(self, globals_ref, locals_ref):

        super().__init__()

        self._globals = globals_ref
        self._locals = locals_ref

    def unstructure_attrs_asdict(self, obj):
        # type: (Any) -> Dict[str, Any]
        """Our version of `attrs.asdict`, so we can call back to us."""
        attrs = obj.__class__.__attrs_attrs__
        dispatch = self._unstructure_func.dispatch
        rv = self._dict_factory()
        for a in attrs:
            name = a.name
            v = getattr(obj, name)
            rv[name] = dispatch(v.__class__)(v)

        # CUSTOM MODIFICATIONS
        if isinstance(obj, tdlib_generated.RootObject):
            rv[constants.TDLIB_JSON_TYPE_STR] = getattr(obj, constants.TDLIB_TYPE_VAR_NAME)
        # END CUSTOM MODIFICATIONS

        return rv


    def structure_attrs_fromdict(self, dict_to_unstructure, cl):
        '''
        @param dict_to_unstructure - a dictionary, the stuff we are deserializing into an actual object
        @param cl - the class provided to converter.structure, however since this is our
            own converter, we are ignoring this and using the types that the JSON has in the
            `@type` key/value
        '''

        # type: (Mapping[str, Any], Type[T]) -> T
        """Instantiate an attrs class from a mapping (dict)."""


        # CUSTOM MODIFICATIONS

        structure_logger.debug("structuring, dict_to_unstructure = `%s`, class = `%s`", dict_to_unstructure, cl)

        actual_type = cl


        if constants.TDLIB_JSON_TYPE_STR in dict_to_unstructure.keys():

            # TODO should extract this to a separate method
            stated_type_in_json = dict_to_unstructure[constants.TDLIB_JSON_TYPE_STR]
            actual_type = eval(stated_type_in_json, self._globals, self._locals)

        structure_logger.debug("using the class `%s` instead of `%s` because `%s` was in the dict we are unstructuring's keys",
            actual_type, cl, constants.TDLIB_JSON_TYPE_STR)

        # END CUSTOM MODIFICATIONS

        # For public use.
        conv_obj = {}  # Start with a fresh dict, to ignore extra keys.
        dispatch = self._structure_func.dispatch
        structure_logger.debug("iterating over attributes of `%s`", actual_type)
        for a in actual_type.__attrs_attrs__:  # type: ignore
            # We detect the type by metadata.
            name = a.name
            type_ = a.type

            structure_logger.debug("-- name: `%s`, type: `%s`", name, type_)
            # CUSTOM MODIFICATIONS
            if isinstance(type_, str):

                # don't use typing.get_type_hints here it doesn't seem to work for strings
                # unless you do it in the place that the class was defined *table flip*
                newtype = eval(type_, self._globals, self._locals)

                structure_logger.debug("---- type is now `%s`, original type was a string, ran eval() on it", newtype)
                type_ = newtype

            if isinstance(dict_to_unstructure, tdlib_generated.RootObject):

                # we need this because technically every message we get back will be a
                # subclass of RootObject, and even smaller stuff like LogStream has several subclasses like
                # `logStreamFile`, but if we use the stated type, we would try and just create the LogStream
                # object which has nothing (as its essentially an interface) rather than the `logStreamFile`
                # that 'is a' LogStream

                # TODO should extract this to a different method
                stated_type_in_json = dict_to_unstructure[constants.TDLIB_JSON_TYPE_STR]
                newtype = eval(stated_type_in_json, self._globals, self._locals)

                structure_logger.debug("---- new type is now `%s`, original type was a subclass of RootObject so we use the type in the dict's `%s` key/value",
                    newtype, constants.TDLIB_JSON_TYPE_STR)

                type_ = newtype

            # END CUSTOM MODIFICATIONS


            try:
                val = dict_to_unstructure[name]
            except KeyError:
                # CUSTOM EDIT
                # see https://github.com/tdlib/td/issues/890
                # basically, tdjson will not return a key/value pair if it is null
                # which causes attrs to complain because every value is mandatory unless
                # it has an explicit default, which would require a huge amount of trial and error, so
                # in this case if we can't find the key/va,ue, just set it to be None for now

                val = None
                structure_logger.debug("for the type `%s`, the key `%s` was missing, substituting it with `%s`", type_, name, None)
                # continue
                #####################################33

            if name[0] == "_":
                name = name[1:]

            structure_logger.debug("---- dispatching to structure type `%s`", type_)

            # CUSTOM EDIT
            # just cleaning this up but the logic should be the same, except now we check for None values as well
            # conv_obj[name] = (
            #     dispatch(type_)(val, type_) if type_ is not None else val
            # )
            if type_ is not None and val is not None:
                conv_obj[name] = dispatch(type_)(val, type_)
            else:
                conv_obj[name] = val
            ########################

        return actual_type(**conv_obj)  # type: ignore


# TAKEN FROM https://github.com/python-attrs/attrs/blob/master/src/attr/_funcs.py
# REVISION: 8824dc26c219abcb43564dd9386fe1a88f938344
def custom_asdict(
    inst,
    recurse=True,
    filter=None,
    dict_factory=dict,
    retain_collection_types=False,
):
    """
    Return the ``attrs`` attribute values of *inst* as a dict.
    Optionally recurse into other ``attrs``-decorated classes.
    :param inst: Instance of an ``attrs``-decorated class.
    :param bool recurse: Recurse into classes that are also
        ``attrs``-decorated.
    :param callable filter: A callable whose return code determines whether an
        attribute or element is included (``True``) or dropped (``False``).  Is
        called with the `attr.Attribute` as the first argument and the
        value as the second argument.
    :param callable dict_factory: A callable to produce dictionaries from.  For
        example, to produce ordered dictionaries instead of normal Python
        dictionaries, pass in ``collections.OrderedDict``.
    :param bool retain_collection_types: Do not convert to ``list`` when
        encountering an attribute whose type is ``tuple`` or ``set``.  Only
        meaningful if ``recurse`` is ``True``.
    :rtype: return type of *dict_factory*
    :raise attr.exceptions.NotAnAttrsClassError: If *cls* is not an ``attrs``
        class.
    ..  versionadded:: 16.0.0 *dict_factory*
    ..  versionadded:: 16.1.0 *retain_collection_types*
    """
    attrs = attr.fields(inst.__class__)
    rv = dict_factory()

    # HACKY: but needed to avoid a recursive import
    from telegram_dl.tdlib_generated import RootObject

    for a in attrs:
        v = getattr(inst, a.name)
        if filter is not None and not filter(a, v):
            continue
        if recurse is True:
            if attr.has(v.__class__):
                tmp = custom_asdict(
                    v, True, filter, dict_factory, retain_collection_types
                )

                # CUSTOM: handle the object being a subclass of RootObject
                if isinstance(v, RootObject):
                    tmp[constants.TDLIB_JSON_TYPE_STR] = getattr(v, constants.TDLIB_TYPE_VAR_NAME)
                    if v._extra:
                        tmp[constants.TDLIB_JSON_EXTRA_STR] = v._extra

                rv[a.name] = tmp

            elif isinstance(v, (tuple, list, set)):
                cf = v.__class__ if retain_collection_types is True else list
                rv[a.name] = cf(
                    [
                        _custom_asdict_anything(
                            i, filter, dict_factory, retain_collection_types
                        )
                        for i in v
                    ]
                )
            elif isinstance(v, dict):
                df = dict_factory
                rv[a.name] = df(
                    (
                        _custom_asdict_anything(
                            kk, filter, df, retain_collection_types
                        ),
                        _custom_asdict_anything(
                            vv, filter, df, retain_collection_types
                        ),
                    )
                    for kk, vv in v.items()
                )
            else:
                rv[a.name] = v
        else:
            rv[a.name] = v

    # CUSTOM: handle top level object is a subclass of RootObject
    if isinstance(inst, RootObject):
        rv[constants.TDLIB_JSON_TYPE_STR] = getattr(inst, constants.TDLIB_TYPE_VAR_NAME)
        if inst._extra:
            rv[constants.TDLIB_JSON_EXTRA_STR] = inst._extra
    return rv

# TAKEN FROM https://github.com/python-attrs/attrs/blob/master/src/attr/_funcs.py
# REVISION: 8824dc26c219abcb43564dd9386fe1a88f938344
def _custom_asdict_anything(val, filter, dict_factory, retain_collection_types):
    """
    ``asdict`` only works on attrs instances, this works on anything.
    """
    if getattr(val.__class__, "__attrs_attrs__", None) is not None:
        # Attrs class.
        rv = custom_asdict(val, True, filter, dict_factory, retain_collection_types)
    elif isinstance(val, (tuple, list, set)):
        cf = val.__class__ if retain_collection_types is True else list
        rv = cf(
            [
                _custom_asdict_anything(
                    i, filter, dict_factory, retain_collection_types
                )
                for i in val
            ]
        )
    elif isinstance(val, dict):
        df = dict_factory
        rv = df(
            (
                _custom_asdict_anything(kk, filter, df, retain_collection_types),
                _custom_asdict_anything(vv, filter, df, retain_collection_types),
            )
            for kk, vv in val.items()
        )
    else:
        rv = val
    return rv

