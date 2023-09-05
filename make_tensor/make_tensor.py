import numpy as np
import logging
import argparse
import pandas as pd
from ..main import register_parser
from ..main import logger

my_logger = logger("make_tensor").logger

def parse_shape(shape_str):
  try:
    shape_list = list(map(int, shape_str.split('x')))
    return tuple(shape_list)
  except ValueError:
    raise argparse.ArgumentTypeError("Invalid shape format. Use 'x' to separate dimensions.")

@register_parser
def add_data_analysis_parser(subparsers):
  """ Include parser for 'print data' subcommand """
  parser = subparsers.add_parser("make_tensor", help="make tesor input")
  parser.set_defaults(func=main)
  parser.add_argument('shape', type=parse_shape, help='shape of the numpy array')
  parser.add_argument('--random', action='store_true', help='generate random data')
  parser.add_argument('--fixed', type=float, help='generate fixed value data')
  parser.add_argument('--pattern', type=str, help='generate data using a pattern')


def zero_one(d1, d2, d3, d4):
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
      if len(shape) != 4:
        raise ValueError("Pattern Mode just support 4d shape")
      if pattern == "d3":
        return np.fromfunction(d3, shape)
      elif pattern == "d2":
        return np.fromfunction(d2, shape)
      elif pattern == "d1":
        return np.fromfunction(d1, shape)
      elif pattern == "d0":
        return np.fromfunction(d0, shape)
      elif pattern == "zero_one":
        return np.fromfunction(zero_one, shape)
      else:
        raise ValueError("Pattern Mode not support")
    elif fixed is not None:
      return np.full(shape, fixed)
    elif random:
      return np.random.random(shape)
    else:
      raise ValueError("Invalid arguments provided.")

def main(args):
  data = create_numpy_array(args.shape, args.random, args.fixed, args.pattern)
  # data_row_index = pd.MultiIndex.from_product([range(s) for s in data.shape[:-1]], names=['d_dim1', 'd_dim2', 'd_dim3'])
  # data_col_index = pd.Index(['col{}'.format(i) for i in range(data.shape[-1])], name='d_cols')
  # data_2d = data.reshape(-1, data.shape[-1])
  # data_2d = np.around(data_2d, decimals=2)
  # data_df = pd.DataFrame(data_2d, index=data_row_index, columns=data_col_index)
  # data_df.to_csv("dtool.log", mode='w', header=True, index=True, sep='\t')
  np.save('data.npy', data)


