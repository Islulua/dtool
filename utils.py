import pandas as pd
import numpy as np
from .main import logger
my_logger = logger("utils").logger

def numpy_to_dataframe(data, row_index=None, col_index=None, depth_index=None, time_index=None, extra_index=None):
    # 获取每个维度的大小
    shape = data.shape
    row_names = [f'dim_{i}' for i in range(len(shape) - 1)]
    
    # 创建索引
    data_row_index = pd.MultiIndex.from_product([range(s) for s in shape[:-1]], names=row_names)
    data_col_index = pd.Index(['col{}'.format(i) for i in range(shape[-1])], name='d_cols')
    # 将多维数组展平为一维，并使用创建的索引
    data_2d = data.reshape(-1, shape[-1])
    # data_2d = np.around(data_2d, decimals=2)
    data_df = pd.DataFrame(data_2d, index=data_row_index, columns=data_col_index)

    return data_df

def print_df(df):
  