# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:01:10 2018

@author: 123
"""
import re
import math
def get_time_ip(x):
### "This function picks out the time and Ip address from each line and if there is a missing value
### in this three variables, just pass it."
### Input: x--list
### Output: (time_list,IP1_list,IP2_list)--tuple
    b=[]
    time_list=[]
    IP1_list=[]
    IP2_list=[]
    for i in range(len(x)):
        try:
            b=re.match(r'([^\s]*) IP ([^\s]*) > ([^\s]*): (.*)$',x[i])
            time_list.append(b.group(1))
            IP1_list.append(b.group(2))
            IP2_list.append(b.group(3))
        except (AttributeError):
            pass
    return time_list,IP1_list,IP2_list


def get_row_number(x):
### This function can print the row numbers of the first line in each minute and store them in d.
### Input: x--list
### Output: d--list
    d=[0]
    for i in range(1,len(x)):
        if x[i].minute!=x[i-1].minute:
            d.append(i)
        else:
            pass
    return d


def percentile(x,n,p):
### "This function calculates the p-percentile value of x"
### Input: x--list; n--integer; p--float
### Output: x[]-- float
    percent=n*p
    if percent%1==0:
        return x[percent-1]
    else:
        return x[math.ceil(percent)-1]


