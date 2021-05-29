##This file contains functions that plots mauna_loa carbon dioxide data

import pandas as pd
import matplotlib.pyplot as plt
def get_df(filename):
    '''
    INPUT:filename e.g. mauna_loa.csv
    OUTPUT: Pandas Dataframe
    '''
    return_df = pd.read_csv(filename)
    return return_df

def plot_df(df):
    '''
    INPUT: Pandas DataFrame
    OUTPUT: handle to plot axis
    '''
    #fig_size = (10, 5)
    #f = plt.figure(figsize=fig_size)
    time = df['decimal_date']-df['decimal_date'][0]\
    
    f= plt.plot(time,df['C02'])
    #f.xlabel('time')
    #f.ylabel('C02')
    return f