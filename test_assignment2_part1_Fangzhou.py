# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:33:17 2018

@author: 123
"""

import datetime
import assignment2_Fangzhou as a2_func

### 1.1
import gzip
with gzip.open('maccdc2012_00016.txt.gz','rb') as f:
    file_content=[x.rstrip().decode() for x in f] ### delete the spare strings on the end and decode the strings 

### use defined function to get the time and ip address of the list
time_ip=a2_func.get_time_ip(file_content)
time_ip=list(time_ip)
time=list(time_ip[0])
ip1=list(time_ip[1])
ip2=list(time_ip[2])

### create a t-list to change the type of time list from str to datetime 
t=[]
for i in range(len(time)):
    t.append(datetime.datetime.strptime(time[i],"%H:%M:%S.%f"))

### create a row_number list to hold the row number of each minute's first Id
row_number=a2_func.get_row_number(t)
row_number.append(4107654)

### calculate the distinct Ip for each minute
Ip1=[]
Ip2=[]
Ip=[]
### use the set command to get rid of the repeated values
for i in range(1,len(row_number)):
    Ip1.append(set(ip1[row_number[i-1]:row_number[i]]))
    Ip2.append(set(ip2[row_number[i-1]:row_number[i]]))
### use | to get the union of two sets
    Ip.append(len(Ip1[i-1]|Ip2[i-1]))
print('the number of distinct IP addresses appearing within each minute:','\n',Ip)


### 1.2 Percentile
### rank the values in list Ip from small to large
Ip_sort=sorted(Ip)
### use defined function to calculate the percentile
### 10th percentile
percent_10th=a2_func.percentile(Ip_sort,len(Ip),0.1)
print('10th percentile:',percent_10th)
### 25th percentile
percent_25th=a2_func.percentile(Ip_sort,len(Ip),0.25)
print('25th percentile:',percent_25th)
### 75th percentile
percent_75th=a2_func.percentile(Ip_sort,len(Ip),0.75)
print('75th percentile:',percent_75th)
### 90th percentile
percent_90th=a2_func.percentile(Ip_sort,len(Ip),0.9)
print('90th percentile:',percent_90th)


### 1.3
### combine all IPs 
all_ip=ip1+ip2
### create a 'times' dictionary to count the number of repetition of a distinct IP
times={}
for i in range(len(all_ip)):
    if all_ip[i] in times:
        times[all_ip[i]]=times[all_ip[i]]+1 ### If all_ip[i] is in the dictionary, plus 1 to show that it appears again
    else:
        times[all_ip[i]]=1 ### If all_ip[i] is not in the dictionary, let its key's value equals to 1 to show it is the first time to appear

### create a 'mean_times' list to calculate the mean value of  the number of distinct IP per minute
mean_times=list(times.values())
for i in range(len(mean_times)):
    mean_times[i]=mean_times[i]/155
### create a list to hold the distinct IPs
Unique_Ip=list(times.keys())
### create a dictionary to show the mean numbers of times each Ip appears
mean_times_dic={}
for i in range(len(Unique_Ip)):
    mean_times_dic[Unique_Ip[i]]=mean_times[i]
print('Mean number of times that each IP address appears within a minute:','\n',mean_times_dic)


### 1.4
### rank the values in list mean_times from small to large
mean_times.sort()
### 10th percentile
times_10th=a2_func.percentile(mean_times,len(mean_times),0.1)
print('10th percentile:',times_10th)
### 25th percentile
times_25th=a2_func.percentile(mean_times,len(mean_times),0.25)
print('25th percentile:',times_25th)
### 75th percentile
times_75th=a2_func.percentile(mean_times,len(mean_times),0.75)
print('75th percentile:',times_75th)
### 90th percentile
times_90th=a2_func.percentile(mean_times,len(mean_times),0.9)
print('90th percentile:',times_90th)