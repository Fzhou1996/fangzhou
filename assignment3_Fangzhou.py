# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 15:16:43 2018

@author: 123
"""

def myfloat(x):
### convert strings containing numbers into actual numbers 
### and use NaN values to represent these missing values in numeric form.
    try:
        return float(x)
    except ValueError:
        return float('nan')