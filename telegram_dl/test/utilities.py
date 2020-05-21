import json
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL


from telegram_dl import utils
from telegram_dl import tdlib_generated as tdg


def get_fake_tdlib_messages_path(partial_path:pathlib.Path) -> pathlib.Path:
    '''
    given a partial path, return a the full path to load a "fake tdlib message"

    so if the fake message file you want is in `<source_root>/telegram_dl/tests/fake_messages/1.json",
    you pass in `1.json` and you get back the full path
    '''

    fake_tdlib_messages_path_prefix = pathlib.Path(f"{__file__}/../fake_tdlib_messages/")

    final_path = fake_tdlib_messages_path_prefix / partial_path

    final_path = final_path.resolve()

    return final_path

def get_testing_sqla_engine():

    # The sqlite :memory: identifier is the default if no filepath is present. Specify sqlite:// and nothing else:
    url = URL(drivername="sqlite",
        username=None,
        password=None,
        host=None,
        port=None,
        database=None,
        query=None)
    e = create_engine(url, echo=False)

    return e

def get_testing_sqla_sessionmaker():

    engine = get_testing_sqla_engine()

    sm = sessionmaker(bind=engine)

    return sm

def load_tdlib_generated_obj_from_file(
    file_path:pathlib.Path, converter:utils.CustomCattrConverter) -> tdg.RootObject:
    '''

    loads a file that contains a JSON representation of a tdlib_generated object

    and 'structure's it using `cattrs` and then returns the object
    '''

    json_text = None
    with open(file_path, "r", encoding="utf-8") as f:
        json_text = f.read()

    json_dict = json.loads(json_text)

    tdg_root_obj = converter.structure(json_dict, tdg.RootObject)

    return tdg_root_obj