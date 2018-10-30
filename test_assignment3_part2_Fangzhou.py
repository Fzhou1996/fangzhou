# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:53:47 2018

@author: 123
"""
import numpy as np
import pandas as pd

### 2.1
### randomly select 365 values from 0 to 100
values=np.random.randint(0,100,(365,))
### get the date 
dates=pd.date_range('20180101', periods=365)
### from date get year,month,day,weekday 
Year=np.array(dates.year)
Month=np.array(dates.month)
Day=np.array(dates.day)
Weekday=[]
for i in dates:
    Weekday.append(i.weekday())
Weekday=np.array(Weekday)
### combine those arrays to dataframe
dailyValues1=pd.DataFrame({'Year':Year,'Month':Month,'Day':Day,'Weekday':Weekday,'Values':values})
### name the month and weekday
dailyValues1.Month=dailyValues1.Month.replace([1,2,3,4,5,6,7,8,9,10,11,12],['January','February','March','April','May','June','July','August','September','October','November','December'])
dailyValues1.Weekday=dailyValues1.Weekday.replace([0,1,2,3,4,5,6],['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])


### 2.2
### redefine a dataframe use month and day as index
dailyValues2=dailyValues1.pivot(index='Month',columns='Day',values='Values')
### reindex in order to sort the month
dailyValues2=dailyValues2.reindex(['January','February','March','April','May','June','July','August','September','October','November','December'])
