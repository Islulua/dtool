import numpy as np
import logging
import argparse
import pandas as pd
from ..main import register_parser
from ..main import logger
from ..utils import numpy_to_dataframe 

my_logger = logger("print_tensor").logger

@register_parser
def add_data_analysis_parser(subparsers):
  """ Include parser for 'print tensor' subcommand """
  parser = subparsers.add_parser("print_tensor", help="print tensor as df")
  parser.set_defaults(func=main)
  parser.add_argument('name', type=str, help='name of the tensor')


def main(args):
  my_logger.info("tensor name={}".format(args.name))
  # load the data
  # Load the data from the .npy file (assuming the .npy file exists)
  try:
    data = np.load(args.name)  # Load the data from the .npy file
  except FileNotFoundError:
    my_logger.error(f"File {args.name}.npy not found.")
    return
  df = numpy_to_dataframe(data)
  df.to_csv("dtool.log", mode='a', sep='\t')
  


