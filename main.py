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
  def __init__(self, name):
    logging.basicConfig(filename='network_debug.log', filemode='w', level=msg_level, style='{')
    self.logger = logging.getLogger(name)
    self.formatter = logging.Formatter(fmt=FMT, datefmt=DATEFMT)
    self.log_filename = '{0}{1}.log'.format(PATH, strftime("%Y-%m-%d"))

    # self.logger.addHandler(self.get_file_handler(self.log_filename))
    self.logger.addHandler(self.get_console_handler())
    # set default level
    self.logger.setLevel(logging.DEBUG)

  # handler to file
  def get_file_handler(self, filename):
    filehandler = logging.FileHandler(filename, encoding="utf-8")
    filehandler.setFormatter(self.formatter)
    return filehandler

  # handler to console
  def get_console_handler(self):
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(self.formatter)
    return console_handler

def main():
  sys.exit(_main(sys.argv[1:]))

if __name__ == "__main__":
  main()
