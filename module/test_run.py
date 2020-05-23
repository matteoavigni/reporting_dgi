# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:45:53 2020

@author: matte
"""

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

tmp = pd.read_csv('https://github.com/matteoavigni/reporting_dgi/raw/master/dataset.csv',sep=';', error_bad_lines=False)
tmp.date = [datetime.strptime(x,'%d/%m/%Y') for x in tmp.date]
returns = tmp.set_index('date')

corr_matrix = returns.corr()



for i in range(len(corr_matrix)):
    for j in range(len(corr_matrix)):
        if j>i:
            corr_matrix.iloc[i,j] = 0

f = plt.figure(figsize=(14,10))
ax = plt.gca()
im = ax.matshow(corr_matrix, cmap='RdBu', vmin=-1, vmax=1)
ax.set_xticks(range(returns.shape[1]))
ax.set_xticklabels(returns.columns)
ax.set_yticks(range(returns.shape[1]))
ax.set_yticklabels(returns.columns)
ax.xaxis.set_ticks_position('bottom')
# Rotate and align 
plt.setp([tick.label1 for tick in ax.xaxis.get_major_ticks()], rotation=60,
         ha="right", va="center", rotation_mode="anchor", size=15)
plt.setp([tick.label1 for tick in ax.yaxis.get_major_ticks()], rotation=0,
          size=15)

#            for tick in ax.xaxis.get_major_ticks():
#                tick.label.set_fontsize(14) 
                
cb = f.colorbar(im)
cb.ax.tick_params(labelsize=14)
ax.set_title('Correlation Matrix', fontsize=16);


