# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:19:15 2020

@author: matte

DESCRIPTION: this module contains the correlation matrix object
"""
import matplotlib.pyplot as plt
import pandas as pd
import copy


import functions


class CorrMatrix:
    def __init__(self, data):
        """
        DESCRIPTION: this function initialize attributes of the class
        INPUT:
            returns = matrix of data on which compute correlations. Columns are
                        the variables (pandas.DataFrame)
        """
        self.data = data
        self.correlations = data.corr()
        self.variables = data.columns.tolist()
        self.pvals = functions.compute_pearsons_pvalues_matrix(self.data)

    def get_correlation_matrix(self):
        """
        DESCRIPTION: this function plot the correlation matrix
        OUTPUT:
            f = correlation matrix as a plot (matplotlib.figure.Figure)
        """
        # leaving just the low-left matrix
        plt.ioff()
        df_corr = copy.deepcopy(self.correlations)
        for i in range(len(df_corr)):
            for j in range(len(df_corr)):
                if j>i:
                    df_corr.iloc[i,j] = 0

        f = plt.figure(figsize=(12,9))
        ax = plt.gca()
        im = ax.matshow(df_corr, cmap='RdBu', vmin=-1, vmax=1)
        ax.set_xticks(range(df_corr.shape[1]))
        ax.set_xticklabels(df_corr.columns)
        ax.set_yticks(range(df_corr.shape[1]))
        ax.set_yticklabels(df_corr.columns)
        ax.xaxis.set_ticks_position('bottom')
        # Rotate and align axis ticks labels
        plt.setp([tick.label1 for tick in ax.xaxis.get_major_ticks()], rotation=60,
                 ha="right", va="center", rotation_mode="anchor", size=15)
        plt.setp([tick.label1 for tick in ax.yaxis.get_major_ticks()], rotation=0,
                  size=15)
                        
        cb = f.colorbar(im)
        cb.ax.tick_params(labelsize=14)
        ax.set_title('Correlation Matrix', fontsize=16)
        
        return f
        
        
    def get_rolling_correlatios(self, var, timeframe):
        """
        DESCRIPTION: this function plot the correlation matrix
        INPUT:
            var = name of the variable to look at (str)
            timeframe = number of periods of the rolling window (int)
        OUTPUT:
            rolling_correlations = correlations for every period and for every other variable (pandas.DataFrame)
            rolling_pvalues = p_values for every period and for every other variable (pandas.DataFrame)
            f = behaviour in time of the correlations (matplotlib.figure.Figure)
        """
        if var not in self.variables:
            raise Exception('\nVariable '+var+' not in the dataset\n')
        if timeframe>len(self.data):
            raise Exception('\nSelected timeframe is too long\n')
        idx = self.data.index.tolist()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
