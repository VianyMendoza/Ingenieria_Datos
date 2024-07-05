import pandas as pd
import numpy as np
import matplotlib as plt
from datetime import datetime
import os

def read_data(file_paths):
    """
    Lee los archivos CSV y devuelve un diccionario de DataFrames.
    """
    dataframes = {}
    for key, path in file_paths.items():
        dataframes[key] = pd.read_csv(path)
    print(dataframes)
    return dataframes


file_paths ={
    'covid' : 'raw\covid.csv',
    'influenza' : 'raw\influenza.csv',
    'dengue' : 'raw\dengue.csv'    
}

dataframes = read_data(file_paths)
