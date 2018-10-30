# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:50:36 2018

@author: 123
"""
import os
import gzip
import math
import statistics
import assignment3_Fangzhou as f3


## get 2000's data
total=[]
for i in os.listdir("2000"):
    with gzip.open("2000/"+i, 'rb') as f:
        file = [x.rstrip().decode() for x in f]
    total.append(file)

### delete the record_count2000.xls.gz
del(total[40])

### get the variables we need
state=[]
structure_number=[]
year_built=[]
year_reconstructed=[]
structure_length=[]
average_daily_traffic=[]

### filter the data we want based on the condition of highway
Index1=[1,4,5,6,7,8]    
for i in range(len(total)):
    for j in range(len(total[i])): 
        if ((math.isnan(f3.myfloat(total[i][j][18])))==False) and ((math.isnan(f3.myfloat(total[i][j][222:228])))==False) and ((math.isnan(f3.myfloat(total[i][j][199])))==False):
            if(int(total[i][j][18])==1) and (float(total[i][j][222:228])>=6.1) and (total[i][j][373]=='Y') and (int(total[i][j][199]) in Index1):
                state.append(f3.myfloat(total[i][j][0:3]))
                structure_number.append(total[i][j][3:18])
                year_built.append(f3.myfloat(total[i][j][156:160]))
                year_reconstructed.append(f3.myfloat(total[i][j][361:365]))
                structure_length.append(f3.myfloat(total[i][j][222:228]))
                average_daily_traffic.append(f3.myfloat(total[i][j][369:371]))

state1=[]
structure_number1=[]
year_built1=[]
year_reconstructed1=[]
structure_length1=[]
average_daily_traffic1=[]

### delete the nan value
for i in range(len(state)):
    if ((math.isnan(state[i]))==False) and ((math.isnan(year_built[i]))==False) and((math.isnan(year_reconstructed[i]))==False) and ((math.isnan(structure_length[i]))==False) and ((math.isnan(average_daily_traffic[i]))==False):
                state1.append(state[i])
                structure_number1.append(structure_number[i])
                year_built1.append(year_built[i])
                year_reconstructed1.append(year_reconstructed[i])
                structure_length1.append(structure_length[i])
                average_daily_traffic1.append(average_daily_traffic[i])

### get 2000's List
L_2000=list(map(list,zip(state1,structure_number1,year_built1,
                    year_reconstructed1,structure_length1,average_daily_traffic1)))



### 2005,same as 2000
total_2005=[]
for i in os.listdir("2005"):
    with gzip.open("2005/"+i, 'rb') as f:
        file = [x.rstrip().decode() for x in f]
    total_2005.append(file)
del(total_2005[40])

state=[]
structure_number=[]
year_built=[]
year_reconstructed=[]
structure_length=[]
average_daily_traffic=[]
Index1=[1,4,5,6,7,8]    
for i in range(len(total_2005)):
    for j in range(len(total_2005[i])): 
        if ((math.isnan(f3.myfloat(total_2005[i][j][18])))==False) and ((math.isnan(f3.myfloat(total_2005[i][j][222:228])))==False) and ((math.isnan(f3.myfloat(total_2005[i][j][199])))==False):
            if(int(total_2005[i][j][18])==1) and (float(total_2005[i][j][222:228])>=6.1) and (total_2005[i][j][373]=='Y') and (int(total_2005[i][j][199]) in Index1):
                state.append(f3.myfloat(total_2005[i][j][0:3]))
                structure_number.append(total_2005[i][j][3:18])
                year_built.append(f3.myfloat(total_2005[i][j][156:160]))
                year_reconstructed.append(f3.myfloat(total_2005[i][j][361:365]))
                structure_length.append(f3.myfloat(total_2005[i][j][222:228]))
                average_daily_traffic.append(f3.myfloat(total_2005[i][j][369:371]))

state1=[]
structure_number1=[]
year_built1=[]
year_reconstructed1=[]
structure_length1=[]
average_daily_traffic1=[]

for i in range(len(state)):
    if ((math.isnan(state[i]))==False) and ((math.isnan(year_built[i]))==False) and((math.isnan(year_reconstructed[i]))==False) and ((math.isnan(structure_length[i]))==False) and ((math.isnan(average_daily_traffic[i]))==False):
                state1.append(state[i])
                structure_number1.append(structure_number[i])
                year_built1.append(year_built[i])
                year_reconstructed1.append(year_reconstructed[i])
                structure_length1.append(structure_length[i])
                average_daily_traffic1.append(average_daily_traffic[i])

L_2005=list(map(list,zip(state1,structure_number1,year_built1,
                    year_reconstructed1,structure_length1,average_daily_traffic1)))

### 2010,same as 2005&2000
total_2010=[]
for i in os.listdir("2010"):
    with gzip.open("2010/"+i, 'rb') as f:
        file = [x.rstrip().decode() for x in f]
    total_2010.append(file)

### delete the record_count2010.xls.gz
del(total_2010[0])

state=[]
structure_number=[]
year_built=[]
year_reconstructed=[]
structure_length=[]
average_daily_traffic=[]
Index1=[1,4,5,6,7,8]    
for i in range(len(total_2010)):
    for j in range(len(total_2010[i])): 
        if ((math.isnan(f3.myfloat(total_2010[i][j][18])))==False) and ((math.isnan(f3.myfloat(total_2010[i][j][222:228])))==False) and ((math.isnan(f3.myfloat(total_2010[i][j][199])))==False):
            if(int(total_2010[i][j][18])==1) and (float(total_2010[i][j][222:228])>=6.1) and (total_2010[i][j][373]=='Y') and (int(total_2010[i][j][199]) in Index1):
                state.append(f3.myfloat(total_2010[i][j][0:3]))
                structure_number.append(total_2010[i][j][3:18])
                year_built.append(f3.myfloat(total_2010[i][j][156:160]))
                year_reconstructed.append(f3.myfloat(total_2010[i][j][361:365]))
                structure_length.append(f3.myfloat(total_2010[i][j][222:228]))
                average_daily_traffic.append(f3.myfloat(total_2010[i][j][369:371]))

state1=[]
structure_number1=[]
year_built1=[]
year_reconstructed1=[]
structure_length1=[]
average_daily_traffic1=[]

for i in range(len(state)):
    if ((math.isnan(state[i]))==False) and ((math.isnan(year_built[i]))==False) and((math.isnan(year_reconstructed[i]))==False) and ((math.isnan(structure_length[i]))==False) and ((math.isnan(average_daily_traffic[i]))==False):
                state1.append(state[i])
                structure_number1.append(structure_number[i])
                year_built1.append(year_built[i])
                year_reconstructed1.append(year_reconstructed[i])
                structure_length1.append(structure_length[i])
                average_daily_traffic1.append(average_daily_traffic[i])

L_2010=list(map(list,zip(state1,structure_number1,year_built1,
                    year_reconstructed1,structure_length1,average_daily_traffic1)))

### combine the 3 lists
L=L_2000+L_2005+L_2010


### 1.1
### write a dict to count the number of bridges
numbers={}
for i in range(len(L)):
    if L[i][0] in numbers:
        numbers[L[i][0]]=numbers[L[i][0]]+1
### If the state is in the dictionary, plus 1 to show that it appears again
    else:
        numbers[L[i][0]]=1
### find the key of the max value
stateWithMostBridges=max(numbers,key=numbers.get)


### 1.2
### write a dict to sum up the structure length
avgLenBridges1={}
avgLenBridges1={L[0][0]:L[0][4]}
for i in range(len(L)):
    if L[i][0] in avgLenBridges1:
        avgLenBridges1[L[i][0]]+=L[i][4] 
### If the state is in the dictionary, plus its structure length to show that it appears again
    else:
        avgLenBridges1[L[i][0]]=L[i][4]
### create dict avgLenBridges to calculate the average length of each state
avgLenBridges={i:float(avgLenBridges1[i]/numbers[i]) for i in numbers}


### 1.3 
### find the key of the max value
shortLongStates=(min(avgLenBridges,key=avgLenBridges.get),max(avgLenBridges,key=avgLenBridges.get))


### 1.4
### write a dict to get the time from built to reconstructed
duration=[]
for i in range(len(structure_length1)):
    if L[i][3]-L[i][2]>=0:### if the difference >=0,it shows that it was reconstructed
        duration.append(L[i][3]-L[i][2])### get the time
avgRebuilt=statistics.mean(duration)### get the mean time    


### 1.5
### create a dict to get the 2000's daily_traffic of each bridge based on the structure_number
bridge_traffic={}
for i in range(len(L_2000)):
    bridge_traffic[L_2000[i][1]]=L_2000[i][5]
    
### create a dict to get the daily_traffic change from 2000 to 2010
for i in range(len(L_2010)):
    if L_2010[i][1] in bridge_traffic:
        bridge_traffic[L_2010[i][1]]-=L_2010[i][5]
    else:
        pass

### get the values of the number of increased daily_traffic 
change=list(bridge_traffic.values())
increase=[]
for i in range(len(change)):
    if change[i]<0:
        increase.append(1)
### get the propotion
propIncTraffic=len(increase)/len(bridge_traffic)
 

### 1.6
### create a dict to get the 2000's daily_traffic that in the dict above
bridge_unique=list(bridge_traffic.keys())
bridge_unique[i]
bridge_traffic1={}
for i in range(len(L_2000)):
    if L_2000[i][1] in bridge_traffic:
        bridge_traffic1[L_2000[i][1]]=L_2000[i][5]
### create a dict to get the daily_traffic change's percent that in the dict above
bridge_traffic2={}        
for i in range(len(bridge_traffic)):
    if bridge_traffic1[bridge_unique[i]]==0:
        if bridge_traffic[bridge_unique[i]]!=0:
            bridge_traffic2[bridge_unique[i]]=10 ### define: change percent x/0=10
        else:
            bridge_traffic2[bridge_unique[i]]=0  ### define: change percent 0/0=0
    else:
        bridge_traffic2[bridge_unique[i]]=-(bridge_traffic[bridge_unique[i]]/bridge_traffic1[bridge_unique[i]])
avgPercentChange=statistics.mean(list(bridge_traffic2.values()))### get the average percent change
