# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:34:58 2018

@author: 123
"""

### 1.1
import assignment1_Data as a1Data
crime=a1Data.get_US_crime()

### 1.2
import assignment1_Fangzhou as a1Func
print("Is it true that the lists inside the crimes list have the same number of elements?",
      a1Func.equal_length(crime),'\n')

### 1.3
name_of_states=a1Func.get_states(crime)
print(name_of_states,'\n')

### 1.4
print("Is it true that the total number of violent crimes is equal to the ‘Violent crime total’?", 
      a1Func.equal_vc(crime),'\n')
print("Is it true that the total number of property crimes is equal to the ‘Property crime total’?",
      a1Func.equal_pc(crime),'\n')

### 1.5
print("Is it true that US total values correspond to the sum of reported values for all states?",
      a1Func.equal_total(crime),'\n')

### 1.6
crimeRates=a1Func.get_crime_rate(crime)
print(crimeRates,'\n')

### 1.7
crimeRatesOriginal=a1Data.get_US_crime_rates()
a1Func.equal_rates(lst1=crimeRates,lst2=crimeRatesOriginal,n=3)

### 1.8
print(a1Func.top5_violent_states(crimeRates),'\n')

### 1.9
print(a1Func.top_crime_states(lst=crimeRates,Crime='Rape',n=6),'\n')

### 1.10
a1Func.crime_stats(lst=crimeRates,Crime='Burglary')