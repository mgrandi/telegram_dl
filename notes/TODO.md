

TODO:

edit db_model classes to make it so we can specify `primary_key=True` on the PK columns and have an empty
PrimaryConstraint for naming it
see:
```plaintext
New in version 0.9.2: an empty PrimaryKeyConstraint may now be specified for the purposes of establishing keyword arguments with the constraint, independently of the specification of “primary key” columns within the Table itself; columns marked as primary_key=True will be gathered into the empty constraint’s column collection.

https://docs.sqlalchemy.org/en/13/core/constraints.html?highlight=primarykeyconstraint#sqlalchemy.schema.PrimaryKeyConstraint
```

apparently messages can be edited to be one content type to another, see message with tg_message_id of `2295332864`
* SOLVED, turns out message ids are only unique to the chat they belong to

make it so cattrs / whatever i use is solely responsible for type conversions , instead of between cattrs and a custom
JSON serializer object, aka put it in `utils.register_custom_types_with_cattr_converter`

make it so in handlers, all the stuff that subclasses tdlib_generated.Update is in its own handler
so like updateNewChat, updateNewMessage, etc
probably needs a custom 'functools.methoddispatch' to handle class heirarchies instead of just
raw class identity

Handle FullUserInfo / FullBasicGroupInfo / FullSuperGroupInfo

https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_user_full_info.html
https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1get_user_full_info.html
https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1user_full_info.html


make all the alembic revisions use the batch migration stuff

so stuff like private_chat has a user_id that chat is with, i used to have that foreign key to
user.user_id but that isn't the same value, user_id is the primary key auto increment and tg_user_id is the actual telegram user id, i CAN foreign key it to the correct column (private_chat.user_id -> user.tg_user_id) but then user has multiple entries PER user since it has as_of, will this evne work? do i make a association table or something to handle this? Like a table that is just `User table, user_id, tg_user_id`, and then that pk will go to go to a new table, `user_versions` or something?? this probably also is a thing for 'all' versioned tables i am going to have

for our connection open listener, `sqlalchemy_pool_on_connect_listener`, that only works if we are using sqlite
as a database, we should probably check to make sure we are using sqlite before attaching that listener, aka in
application.py

check out poetry instead of pipenv?

get the version of the app dynamically, maybe using something like this:
https://github.com/pypa/setuptools_scm/
https://github.com/pypa/setuptools_scm/#retrieving-package-version-at-runtime
https://pypi.org/project/importlib-metadata/ (or just the importlib library included in python 3.8?)

handle updateConnectionState

RootObject doesn't need _extra_ as an attrib, as that is only on the top most object

look into cattrs and figure out how to maybe use a converter to add the @type JSON keys for every object recursively? https://cattrs.readthedocs.io/en/latest/converters.html right now i have no way to turn the JSON i get back from tdjson into an object



should i be using singledispatchmethod instead of single dispatch?


how does the 'extra' fit in? am i going to need to figure out what message i receive goes with what request i send?


https://github.com/tdlib/td/issues/890


maybe extend single dispatch to include class heirarchy? so like all Update subclasses go to X method?



need to make it so alembic runs when the script runs, takes values from our config, can construct the alembic config programmatically
    https://alembic.sqlalchemy.org/en/latest/api/config.html



maybe just get rid of TdlibResult ?


figure out how i want to deal with this callback mechanism that tdlib wants me to use, how does that fit into 'extra'?

add 'as of' date column to stuff that will be versioned, sqlalchemy_utils i think has a mixin for this? research mixins? maybe a Versioned mixin?



create github issue for sqlalchemy_utils where if you don't create an instance of the class you have a 'impl' of in ChoiceType
then it throws asuper confusing exception

# good
sqlalchemy_utils.types.choice.ChoiceType(dbme.LinkStateEnum, impl=Integer())

# bad
sqlalchemy_utils.types.choice.ChoiceType(dbme.LinkStateEnum, impl=Integer)

# causes:
Traceback (most recent call last):
  File "C:\Python38\Lib\runpy.py", line 192, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Python38\Lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "~\.virtualenvs\telegram_dl-lBVcTN7c\Scripts\alembic.exe\__main__.py", line 7, in <module>
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\config.py", line 575, in main
    CommandLine(prog=prog).main(argv=argv)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\config.py", line 569, in main
    self.run_cmd(cfg, options)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\config.py", line 546, in run_cmd
    fn(
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\command.py", line 298, in upgrade
    script.run_env()
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\script\base.py", line 489, in run_env
    util.load_python_file(self.dir, "env.py")
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\util\pyfiles.py", line 98, in load_python_file
    module = load_module_py(module_id, path)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\util\compat.py", line 173, in load_module_py
    spec.loader.exec_module(module)
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "~\Code\personal\telegram_dl\telegram_dl\alembic\env.py", line 86, in <module>
    run_migrations_online()
  File "~\Code\personal\telegram_dl\telegram_dl\alembic\env.py", line 80, in run_migrations_online
    context.run_migrations()
  File "<string>", line 8, in run_migrations
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\runtime\environment.py", line 846, in run_migrations
    self.get_context().run_migrations(**kw)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\runtime\migration.py", line 518, in run_migrations
    step.migration_fn(**kw)
  File "~\Code\personal\telegram_dl\telegram_dl\alembic\versions\ffbee41f3a35_20200121_add_user_file_profile_photo_tables.py", line 35, in upgrade
    op.create_table('user',
  File "<string>", line 8, in create_table
  File "<string>", line 3, in create_table
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\operations\ops.py", line 1250, in create_table
    return operations.invoke(op)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\operations\base.py", line 345, in invoke
    return fn(self, operation)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\operations\toimpl.py", line 101, in create_table
    operations.impl.create_table(table)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\ddl\impl.py", line 252, in create_table
    self._exec(schema.CreateTable(table))
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\alembic\ddl\impl.py", line 134, in _exec
    return conn.execute(construct, *multiparams, **params)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\engine\base.py", line 982, in execute
    return meth(self, multiparams, params)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\ddl.py", line 72, in _execute_on_connection
    return connection._execute_ddl(self, multiparams, params)
    compiled = ddl.compile(
  File "<string>", line 1, in <lambda>
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\elements.py", line 462, in compile
    return self._compiler(dialect, bind=bind, **kw)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\ddl.py", line 29, in _compiler
    return dialect.ddl_compiler(dialect, self, **kw)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\compiler.py", line 319, in __init__
    self.string = self.process(self.statement, **compile_kwargs)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\compiler.py", line 350, in process
    return obj._compiler_dispatch(self, **kwargs)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\visitors.py", line 92, in _compiler_dispatch
    return meth(self, **kw)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\compiler.py", line 2873, in visit_create_table
    processed = self.process(
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\compiler.py", line 350, in process
    return obj._compiler_dispatch(self, **kwargs)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\visitors.py", line 92, in _compiler_dispatch
    return meth(self, **kw)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\compiler.py", line 2906, in visit_create_column
    text = self.get_column_specification(column, first_pk=first_pk)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\dialects\sqlite\base.py", line 1067, in get_column_specification
    coltype = self.dialect.type_compiler.process(
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\compiler.py", line 401, in process
    return type_._compiler_dispatch(self, **kw)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\visitors.py", line 92, in _compiler_dispatch
    return meth(self, **kw)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\compiler.py", line 3416, in visit_type_decorator
    return self.process(type_.type_engine(self.dialect), **kw)
  File "~\.virtualenvs\telegram_dl-lbvctn7c\lib\site-packages\sqlalchemy\sql\compiler.py", line 401, in process
    return type_._compiler_dispatch(self, **kw)
TypeError: _compiler_dispatch() missing 1 required positional argument: 'visitor'