import numpy as np
import logging
import argparse
import pandas as pd
from ..main import register_parser
from ..main import logger
from ..utils import numpy_to_dataframe 

my_logger = logger("make_tensor").logger

def parse_shape(shape_str):
  try:
    shape_list = list(map(int, shape_str.split('x')))
    return tuple(shape_list)
  except ValueError:
    raise argparse.ArgumentTypeError("Invalid shape format. Use 'x' to separate dimensions.")

@register_parser
def add_data_analysis_parser(subparsers):
  """ Include parser for 'make tensor' subcommand """
  parser = subparsers.add_parser("make_tensor", help="make tensor input")
  parser.set_defaults(func=main)
  parser.add_argument('shape', type=parse_shape, help='shape of the numpy array')
  parser.add_argument('--random', action='store_true', help='generate random data')
  parser.add_argument('--fixed', type=float, help='generate fixed value data')
  parser.add_argument('--pattern', type=str, help='generate data using a pattern')


def zero_one(shape):
  return (d1 + d2 + d3 + d4) % 2
def d3(d1, d2, d3, d4):
  return d4
def d2(d1, d2, d3, d4):
  return d3;
def d1(d1, d2, d3, d4):
  return d2;
def d0(d1, d2, d3, d4):
  return d1;

def create_numpy_array(shape, random=False, fixed=None, pattern=None):
    if pattern is not None:
      # TODO: dingtao.lu
      my_logger.error("Pattern Mode not support now")
      raise ValueError("Pattern Mode not support")
    elif fixed is not None:
      my_logger.info("create fixed data, value:{}".format(fixed))
      return np.full(shape, fixed)
    elif random:
      my_logger.info("create random data")
      return np.random.random(shape)
    else:
      raise ValueError("Invalid arguments provided.")

def main(args):
  my_logger.info("shape={}".format(args.shape))
  data = create_numpy_array(args.shape, args.random, args.fixed, args.pattern)
  
  df = numpy_to_dataframe(data)
  df.to_csv("dtool.log", mode='a', sep='\t')

  np.save('data.npy', data)


