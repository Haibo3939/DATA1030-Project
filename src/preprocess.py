# DATA1030 
# Author: Haibo Li

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split

def any_null_col(df):
    """
    check if a dataframe df contains null values (np.nan only)
  
    Parameters:
    df: pandas DataFrame
  
    Returns:
    bool: True if there is at least one null value False, otherwise
  
    """
    null_lst = []
    null_count = 0
    ratios = []
    for c in df.columns:
        if df[c].isnull().any():
            null_lst.append(c)
            null_count += 1
    if null_count > 0:
        
        for col in null_lst:
            ratios.append(count_null_ratio(df, col))
        
        print('Columns containing null values:', null_lst, 'with null ratios:', ratios) 
        return True
   
    print('The table contains no np.nan values')
    return False  


def count_null_ratio(df, col):
    """
    count null ratio of a column in df
    """  
    return np.round(df[col].isnull().sum() / len(df[col]), 3)


def convert_x_to_map(start_x, size_x, res_x, x):
    x += (start_x * -1.0) if (start_x < 0) else start_x
    x = math.floor((x / size_x) * res_x)
    return x

def convert_y_to_map(start_y, size_y, res_y, y):
    y += (start_y * -1.0) if (start_y < 0) else start_y
    y = math.floor((y / size_y) * res_y)
    y = (y - res_y) * -1.0
    return y


def add_coordinates(master_demos, map_data):
    master_demos['AttackPosX'] = np.nan
    master_demos['AttackPosY'] = np.nan


    for map_name in master_demos['map'].unique():
        if map_name not in map_data.index:
            # print(f'Data not found for map: {map_name}')
            continue
        # Pull metadata for the map in question.
        data = map_data.loc[map_name]
        start_x = data['StartX']
        start_y = data['StartY']
        end_x = data['EndX']
        end_y = data['EndY']
        size_x = end_x - start_x
        size_y = end_y - start_y
        res_x = data['ResX']
        res_y = data['ResY']
        
        # Apply the conversion functions to the appropriate columns and store them in the dummy columns created earlier.
        # print(f'Converting coordinates for {map_name}', end='')
        master_demos.loc[master_demos['map'] == map_name, 'AttackPosX'] =  master_demos.loc[master_demos['map'] == map_name, 'att_pos_x'].apply(lambda x: convert_x_to_map(start_x, size_x, res_x, x))
        master_demos.loc[master_demos['map'] == map_name, 'AttackPosY'] =  master_demos.loc[master_demos['map'] == map_name, 'att_pos_y'].apply(lambda y: convert_y_to_map(start_y, size_y, res_y, y))
        # print('...done!')

