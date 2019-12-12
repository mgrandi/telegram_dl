import attr
import json
import pathlib

from telegram_dl import constants

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, pathlib.Path):
            return str(obj)

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

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

