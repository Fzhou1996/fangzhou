# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:09:29 2018

@author: 123
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 3.1
### import data
trips1 = pd.read_csv('trips.csv')

## 3.1.1
### Latitude is greater than 40 and less than 41.5
a=trips1.loc[(trips1.pickup_latitude < 41.5)&(trips1.pickup_latitude > 40)]

## 3.1.2
### Longitude is greater than -75 and less than -72
b=a.loc[(a.pickup_longitude < -72)&(a.pickup_longitude > -75)]

## 3.1.3
### The number of passengers is greater than 0 and less than 5
trips1.dtypes
c=b.loc[(b.passenger_count<5)&(b.passenger_count>0)]

## 3.1.4
### get trips1 under the condition that the trip time in seconds is greater than 1800
trips1=c.loc[c.trip_time_in_secs>1800]


# 3.2
### discribe the trips and print a tuple
trips1_stat=trips1.describe()
tripStats=(len(trips1),trips1_stat.at['mean','passenger_count'],
           trips1_stat.at['mean','trip_time_in_secs'],trips1_stat.at['std','trip_time_in_secs'])



# 3.3
zip_codes=pd.read_csv('zipcodes.csv')
### get the coords of trips and split it to latitude and longitude
Coords=zip_codes.Coords
Coords=Coords.str.split(",",expand=True)

### define a dataframe in order to combine the latitude,longitude and zipcode 
Coords=pd.DataFrame(Coords,dtype=np.float)
Coords.columns=['lat','long']
zip_codes1=pd.concat([zip_codes,Coords],axis=1)

### round the digit of longitude and latitude to 2 in order to match
trips1.pickup_latitude=trips1.pickup_latitude.round(2)
trips1.pickup_longitude=trips1.pickup_longitude.round(2)

### merge two data frames
trips2=pd.merge(trips1,zip_codes1,how='right',
                left_on=[trips1.pickup_latitude,trips1.pickup_longitude],
                right_on=['lat','long'])

### drop Nan
trips2=trips2.dropna(axis=0)



# 3.4
### change the type of pickup_time to datetime and sort the dataframe by it
trips2.pickup_datetime=pd.to_datetime(trips2.pickup_datetime)
trips2.sort_values(by=['pickup_datetime'],ascending=True)
trips2.index=range(len(trips2))

### get day, hour as the keys for groupby
Day=[]
for i in range(len(trips2)):
    Day.append(trips2.pickup_datetime[i].day)
Hour=[]
for i in range(len(trips2)):
    Hour.append(trips2.pickup_datetime[i].hour)
trips2['Hour']=np.array(Hour) 
trips2['Day']=np.array(Day)
### groupby and count the number of trips 
group=trips2.groupby(["Day","Hour","Zipcode"]).nunique()
Count=pd.DataFrame(group.iloc[:,0])

### Rename and Reindex
trips3=Count
trips3=Count.reset_index()
trips3.columns=["day","hour","Zipcode","Count"]

### get the weekday
Weekday=[]
for i in trips3.day:
    Weekday.append(i%7)
    
trips3['Weekday']=np.array(Weekday)
trips3.Weekday=trips3.Weekday.replace([0,1,2,3,4,5,6],['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])




# 3.5
weather=pd.read_csv("weather.csv")
### merge the two dataframes by day and hour
trips4=pd.merge(trips3,weather,how='right',
                left_on=[trips3.day,trips3.hour],
                right_on=[weather.Day,weather.Hour])
### trop NaN values
trips4=trips4.dropna(axis=0)



# 3.6
### drop redundant variables
trips5=trips4.drop(['key_0','key_1','day','hour'],axis=1)


#3.7
### find the zipcodes that show more than once
trips5_group=trips5.groupby("Zipcode").sum()
trips6_num=trips5_group.loc[trips5_group.Count >= 2]
Zipcodes=list(trips6_num.index.values)
### get trips 6 according to the list of zipcodes above
trips6=trips5[trips5.Zipcode.isin(Zipcodes)]


#3.8
### find the total number of taxi trips per hour
group_sum=trips6.groupby(["Hour"]).sum()
### find average temperature per hour
group_mean=trips6.groupby(["Hour"]).mean()
### create X-varible
x_vals = np.arange(0,24,1) 
# create an empty figure.
fig,ax1 = plt.subplots()   

ax1.set_xlabel('hours')
ax1.set_ylabel('total trips',color='blue')
ax1.plot(x_vals,group_sum.Count,color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
# instantiate a second axes that shares the same x-axis
ax2 = ax1.twinx()  
ax2.set_ylabel('average temperature',color='red') # we already handled the x-label with ax1
ax2.plot(x_vals, group_mean.Temp, color='red')
ax2.tick_params(axis='y', labelcolor='red')
### otherwise the right y-label is slightly clipped
fig.tight_layout() 
plt.show()



















