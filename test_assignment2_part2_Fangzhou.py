# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:14:01 2018

@author: 123
"""

import numpy as np
import matplotlib.pyplot as plt
### 2.1
aCF=np.loadtxt('adverseCountsFinal.txt',dtype=np.int64)

### 2.2
### Number of 'Serious' side effect
serious_sum=np.sum(aCF[:,1])
print('Serious side effect: ',serious_sum)
### Number of 'Death' side effect
death_sum=np.sum(aCF[:,2])
print('Death side effect: ',death_sum)
### Number of 'Nonserious' side effect
nonserious_sum=np.sum(aCF[:,3])
print('Nonserious side effect: ',nonserious_sum)

### 2.3
side_effect_per_year=(serious_sum+death_sum+nonserious_sum)/len(aCF)
print('Side effects reported per year: ',side_effect_per_year)

### 2.4
### Highest 'Serious' side effect
highest_serious=aCF[np.argmax(aCF[:,1]),0]
print('Year of highest serious side effects: ',highest_serious)
### Highest 'Death' side effect
highest_death=aCF[np.argmax(aCF[:,2]),0]
print('Year of highest death side effect: ',highest_death)
### Highest 'Nonserious' side effect
highest_nonserious=aCF[np.argmax(aCF[:,3]),0]
print('Year of highest nonserious side effects: ',highest_nonserious)

### 2.5
side_effect=aCF[:,1:4]
### add a row which shows the side effect's name
name=np.array(['Serious','Death','Nonserious']).reshape(1,3)
### find the highest side effect for each year
which_effect=side_effect.argmax(axis=1)
### combine the year with the side effect
side_effect=np.concatenate((side_effect,name),axis=0)
### print the year and the type of side effects
np.dstack((aCF[:,0],side_effect[51,which_effect]))

### 2.6
effect=aCF[:,1:4]
aCF_1=effect.copy()
###  get the total number of side effects per year
effect_sum=np.sum(effect,axis=1).reshape(51,1)
### normalize the side effect counts
aCF_1=aCF_1/effect_sum
### get the array of years from 1968 to 2018
year=aCF[:,0].reshape(51,1)
### merge the array 'year' and aCF_1 
side_effect_per=np.concatenate((year,aCF_1),axis=1)
### add the name of each variable
name1=np.array(['Year','Serious','Death','Nonserious']).reshape(1,4)
### merge the array 'name1' and 'side_effect_per'
side_effect_per=np.concatenate((name1,side_effect_per),axis=0)
print('Side effect counts per year:','\n',side_effect_per)

### 2.7
labels=['Serious','Death','Nonserious']
plt.stackplot(aCF[:,0],aCF[:,1],aCF[:,2],aCF[:,3],labels=labels)
plt.xlabel('year')
plt.legend(loc='upper left')
plt.show()