 #!/usr/bin/env python3

# library imports
import argparse
import logging
import sys
import pathlib

# third party imports
import arrow
import attr
import logging_tree
import pyhocon

from telegram_dl.application import Application


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

    resolved_path = pathlib.Path(stringArg).resolve()
    if not resolved_path.exists:
        raise argparse.ArgumentTypeError("The path {} doesn't exist!".format(resolved_path))

    conf = None
    try:
        conf = pyhocon.ConfigFactory.parse_file(str(resolved_path))
    except Exception as e:
        raise argparse.ArgumentTypeError(
            "Failed to parse the file `{}` as a HOCON file due to an exception: `{}`".format(resolved_path, e))

    return conf

if __name__ == "__main__":
    # if we are being run as a real program

    parser = argparse.ArgumentParser(
        description="__^__description__^__",
        epilog="Copyright @date - Mark Grandi")

    # set up logging stuff
    logging.captureWarnings(True) # capture warnings with the logging infrastructure
    root_logger = logging.getLogger()
    logging_formatter = ArrowLoggingFormatter("%(asctime)s %(threadName)-10s %(name)-20s %(levelname)-8s: %(message)s")
    logging_handler = logging.StreamHandler(sys.stdout)
    logging_handler.setFormatter(logging_formatter)
    root_logger.addHandler(logging_handler)



    parser.add_argument('config', type=hocon_config_file_type, help="the configuration file")
    parser.add_argument("--verbose", action="store_true", help="Increase logging verbosity")



    try:
        parsed_args = parser.parse_args()

        # set logging level based on arguments
        if parsed_args.verbose:
            root_logger.setLevel("DEBUG")
        else:
            root_logger.setLevel("INFO")

        root_logger.debug("Parsed arguments: %s", parsed_args)
        root_logger.debug("Logger hierarchy:\n%s", logging_tree.format.build_description(node=None))

        # run the application
        app = Application(parsed_args)
        app.run()

        root_logger.info("Done!")
    except Exception as e:
        root_logger.exception("Something went wrong!")
        sys.exit(1)