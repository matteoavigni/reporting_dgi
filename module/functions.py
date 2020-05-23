# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:39:15 2020

@author: matte

DESCRIPTION: this module contains auxiliary functions used in several other modules
"""

from scipy import stats
import pandas as pd


def compute_pearsons_pvalues_matrix(data):
    """
    DESCRIPTION: this function returns a metrix containing the Pearsons P-values
                of the Pearsons correlations of the data
    INPUT:
        data = dataset to look at (pandas.DataFrame)
    OUTPUT:
        pval = Pearsons P-values (pandas.DataFrame)
    """
    variables = data.columns.tolist()
    pvals = pd.DataFrame(index=variables, columns=variables)
    for n1 in variables:
        for n2 in variables:
            tmp, pvals.loc[n1,n2] = stats.pearsonr(data[n1].tolist(),data[n2].tolist())
    return pvals
