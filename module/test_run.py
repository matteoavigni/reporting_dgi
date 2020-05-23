# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:45:53 2020

@author: matte
"""

import pandas as pd
from datetime import datetime

import plotting_functions
import calculation_functions

import CorrMatrixClass as cmc

##-----------------------------------------------------------------------------
# 0. Setup
##-----------------------------------------------------------------------------
tmp = pd.read_csv('https://github.com/matteoavigni/reporting_dgi/raw/master/module/dataset.csv',sep=';', error_bad_lines=False)
tmp.date = [datetime.strptime(x,'%d/%m/%Y') for x in tmp.date]
returns = tmp.set_index('date')



##-----------------------------------------------------------------------------
# 1. Correlations
##-----------------------------------------------------------------------------
cmc_tot = cmc.CorrMatrix(returns)
fig_corr_matrix = cmc_tot.get_correlation_matrix()














