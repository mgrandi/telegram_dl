 #!/usr/bin/env python3

# library imports
import argparse
import logging
import logging.config
import sys
import pathlib
import asyncio
import json

# third party imports
import attr
import logging_tree

from telegram_dl.application import Application
from telegram_dl import utils


if __name__ == "__main__":
    # if we are being run as a real program

    parser = argparse.ArgumentParser(
        description="__^__description__^__",
        epilog="Copyright @date - Mark Grandi")

    # set up logging stuff
    logging.captureWarnings(True) # capture warnings with the logging infrastructure
    root_logger = logging.getLogger()
    logging_formatter = utils.ArrowLoggingFormatter("%(asctime)s %(threadName)-10s %(name)-20s %(levelname)-8s: %(message)s")
    logging_handler = logging.StreamHandler(sys.stdout)
    logging_handler.setFormatter(logging_formatter)
    root_logger.addHandler(logging_handler)


    parser.add_argument('config', type=utils.hocon_config_file_type, help="the configuration file")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--verbose", action="store_true", help="Increase logging verbosity")
    group.add_argument("--logging-config", dest="logging_config",
        type=utils.isFileType, help="Specify a JSON file representing logging configuration")


    try:
        parsed_args = parser.parse_args()

        # set logging level based on arguments
        if parsed_args.verbose:
            root_logger.setLevel("DEBUG")
        else:
            if parsed_args.logging_config:
                with open(parsed_args.logging_config, "r", encoding="utf-8") as f:
                    logging.config.dictConfig(json.load(f))
            else:
                logging.basicConfig(level="INFO")


        root_logger.debug("Parsed arguments: %s", parsed_args)
        root_logger.debug("Logger hierarchy:\n%s", logging_tree.format.build_description(node=None))

        # run the application
        app = Application(parsed_args)
        asyncio.run(app.run())

        root_logger.info("Done!")
    except Exception as e:
        root_logger.exception("Something went wrong!")
        sys.exit(1)