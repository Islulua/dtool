import argparse
import logging
import sys
import os
import datetime
from time import strftime

REGISTERED_PARSER = []

def register_parser(make_subparser):
  """
  Example
  -------
  @register_parser
  def _example_parser(main_subparser):
      subparser = main_subparser.add_parser('example', help='...')
      ...
  """
  REGISTERED_PARSER.append(make_subparser)
  return make_subparser


def _main(argv):
  parser = argparse.ArgumentParser(
          formatter_class=argparse.RawDescriptionHelpFormatter,
          description="debug tool",
      )
  
  subparser = parser.add_subparsers(title="commands")
  for make_subparser in REGISTERED_PARSER:
    make_subparser(subparser)

  args = parser.parse_args(argv);
  print(args)
  if not hasattr(args, "func"):
    # In case no valid subcommand is provided, show usage and exit
    parser.print_help(sys.stderr)
    return 1

  return args.func(args)


PATH = os.path.abspath('.')
# FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
FMT = '%(levelname)s: %(message)s'
DATEFMT = '%Y-%m-%d %H:%M:%S'

import os
DEBUG_LEVEL = os.environ.get('DTOOL_MSG_LEVEL')
msg_level = ""
if DEBUG_LEVEL == None:
  msg_level = logging.INFO
elif DEBUG_LEVEL == 0:
  msg_level = logging.DEBUG
else:
  msg_level = logging.INFO


class logger:
    def __init__(self, name, log_level=logging.INFO, log_to_file=True, log_to_console=False):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        self.log_format = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        if log_to_file:
            self.log_to_file()
        if log_to_console:
            self.log_to_console()

    def log_to_file(self, log_file='dtool.log'):
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setFormatter(self.log_format)
        self.logger.addHandler(file_handler)

    def log_to_console(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.log_format)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

def main():
  sys.exit(_main(sys.argv[1:]))

if __name__ == "__main__":
  main()
