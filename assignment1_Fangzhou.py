# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 13:03:59 2018

@author: 123
"""
import statistics
import copy
import operator
import random
indexCrime=['Violent crime total','Murder and nonnegligent Manslaughter','Rape',
    'Robbery','Aggravated assault','Property crime total','Burglary','Larceny-theft',
    'Motor vehicle theft']

### 1.2
def equal_length(x):
    for i in range(len(x)):
        if len(x[i])==len(x[0]):
            return True
        else:
            return False

### 1.3       
def get_states(lst):
    states=[]
    for i in range(len(lst)):
        states.append(lst[i][0])
    return(states)

### 1.4
def equal_vc(lst):
    for i in range(len(lst)):
        if lst[i][2]==sum(lst[i][3:7]):
            return True
        else:
            return False
        
def equal_pc(lst):
    for i in range(len(lst)):
        if lst[i][7]==sum(lst[i][8:11]):
            return True
        else:
            return False
       
### 1.5
def equal_total(lst):
    new_lst=copy.deepcopy(lst)
    for i in range(len(lst)-1):
        for j in range(1, len(lst[0])):
            new_lst[i][j]=new_lst[i][j]+new_lst[i+1][j]
    if new_lst[len(lst)-1][1:]==lst[len(lst)-1][1:]:
        return True
    else:
        return False
### 1.6
def get_crime_rate(lst):
    rates=copy.deepcopy(lst)
    for i in range(len(lst)):
        for j in range(2,len(lst[0])):
           rates[i][j]=round(lst[i][j]/lst[i][1]*100000,1)
    return rates

### 1.7 
def equal_rates(lst1,lst2,n):
    a=range(len(lst1))
    b=random.sample(a,n)
    for i in range(n):
        if lst1[b[i]]==lst2[b[i]]:
            print("crimeRates:",lst1[b[i]],"crimeOriginalRates:",lst2[b[i]], True,'\n')
        else:
            print("crimeRates:",lst1[b[i]],"crimeOriginalRates:",lst2[b[i]], False,'\n')
    
    
### 1.8
def top5_violent_states(lst):
     lst.sort(key=operator.itemgetter(2),reverse = True)
     d1={}
     for i in range(0,5):
         d1[lst[i][0]]=lst[i][2]
     return d1

### 1.9
def top_crime_states(lst,Crime,n):
    if Crime in indexCrime:
        lst.sort(key=operator.itemgetter(indexCrime.index(Crime)+2),reverse=True)
        d2={}
        for i in range(0,n):
            d2[lst[i][0]]=lst[i][indexCrime.index(Crime)+2]
        return d2
    else:
        return("Warning!")

### 1.10
def crime_stats(lst,Crime):
    if Crime in indexCrime:
           lst_1=[None]*(len(lst)-1)
           for i in range(len(lst)-1):
               lst_1[i]=lst[i][indexCrime.index(Crime)+2]
           print("mean:",statistics.mean(lst_1))
           print("variance:",statistics.variance(lst_1))
           print("standard deviation:",statistics.stdev(lst_1))
    else:
           print("Warning!")
    

    
