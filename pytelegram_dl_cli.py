 #!/usr/bin/env python3

# library imports
import argparse
import logging
import sys

# third party imports
import arrow
import attr
import requests
import logging_tree


class Application:
    '''__^__description__^__
    '''

    def __init__(self, logger, args):
        ''' constructor
        @param logger the Logger instance
        @param args - the namespace object we get from argparse.parse_args()
        '''

        self.logger = logger
        self.args = args

    def __^__themethod__^__(self):
        self.logger.info("hello world")
        self.logger.debug("hello world debug")
        raise Exception("Testing Exception")



class ArrowLoggingFormatter(logging.Formatter):
    ''' logging.Formatter subclass that uses arrow, that formats the timestamp
    to the local timezone (but its in ISO format)
    '''

    def formatTime(self, record, datefmt=None):
        return arrow.get("{}".format(record.created)).to("local").isoformat()

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


    # silence urllib3 (requests) logger because its noisy
    requests_packages_urllib_logger = logging.getLogger("requests.packages.urllib3")
    requests_packages_urllib_logger.setLevel("INFO")
    urllib_logger = logging.getLogger("urllib3")
    urllib_logger.setLevel("INFO")

    # optional arguments, if specified these are the input and output files, if not specified, it uses stdin and stdout
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="something")
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),default=sys.stdout, help="something")
    parser.add_argument("--verbose", action="store_true", help="Increase logging verbosity")
    parser.add_argument("--dry_run", action="store_true", help="Do a dry run")


    try:
        parsed_args = parser.parse_args()

        # set logging level based on arguments
        if parsed_args.verbose:
            root_logger.setLevel("DEBUG")
        else:
            root_logger.setLevel("INFO")

        root_logger.debug("Parsed arguments: %s", parsed_args)
        root_logger.debug("Logger hierarchy:\n%s", logging_tree.format.build_description(node=None))

        if parsed_args.dry_run:
            root_logger.info("*** Dry Run ***")

        # run the application
        app = Application(root_logger.getChild("app"), parsed_args)
        app.__^__themethod__^__()

        root_logger.info("Done!")
    except Exception as e:
        root_logger.exception("Something went wrong!")
        sys.exit(1)