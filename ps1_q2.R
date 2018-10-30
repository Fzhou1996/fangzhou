library('nycflights13')
airlines13=nycflights13::airlines
airports13=nycflights13::airports
flights13=nycflights13::flights
planes13=nycflights13::planes
weather13=nycflights13::weather
library(dplyr)
# Q2
### a
fl_13=flights13%>%filter(flights13$month<11)
group_airlines_13 = group_by(fl_13, carrier)
airlines_sum_13 = summarize( group_airlines_13,percent=n()/281373)
al13_at_least_0.01=airlines_sum_13%>%filter(airlines_sum_13$percent>0.01)

## b
flights14<-read.csv("E:/506/flights14.csv")
fl_14=subset(flights14,flights14$month<11)
group_airlines_14 = group_by(fl_14, carrier)
airlines_sum_14 = summarize( group_airlines_14,percent=n()/253316)
airlines_13_14=left_join(al13_at_least_0.01,airlines_sum_14,by="carrier")
airlines_13_14$carrier=c('Endeavor Air Inc.','American Airlines Inc.','JetBlue Airways','Delta Air Lines Inc.','ExpressJet Airlines Inc.','AirTran Airways Corporation','Envoy Air','United Air Lines Inc.','US Airways Inc.','Virgin America','Southwest Airlines Co.')


## CI
### The percentage of each airline is Bernoulli distributed.
airlines_13_14[is.na(airlines_13_14)]=0
al_13_14=mutate(airlines_13_14,change=c(airlines_13_14$percent.y-airlines_13_14$percent.x))
f_CI=function(x,n,j,k){L=c();R=c();for(i in j:k){L[i]=x[i]-1.96*sqrt(x[i]*(1-x[i])/n);R[i]=x[i]+1.96*sqrt(x[i]*(1-x[i])/n)};Left=L[1:k];Right=R[1:k];return(cbind(Left,Right))}
### CI of 2013
CI_13=f_CI(al_13_14$percent.x,281373,1,11)
### CI of 2014
CI_14=f_CI(al_13_14$percent.y,253316,1,11)
### CI of change
change_CI=function(x,y,z,n1,n2){L=c();R=c();for(i in 1:11){L[i]=z[i]-1.96*sqrt(x[i]*(1-x[i])/n1+y[i]*(1-y[i])/n2);R[i]=z[i]+1.96*sqrt(x[i]*(1-x[i])/n1+y[i]*(1-y[i])/n2)};Left=L[1:11];Right=R[1:11];return(cbind(Left,Right))}
CI_change=change_CI(al_13_14$percent.x,al_13_14$percent.y,z=al_13_14$change,281373,253316)
### largest increase
al_13_14[which.max(al_13_14$change),1]
### largest decrease
al_13_14[which.min(al_13_14$change),1] 
### table
AL_13_14=cbind(al_13_14,CI_13,CI_14,CI_change)
colnames(AL_13_14)=c("carrier",'percent_13','percent_14','change',"CI_13_Left",'CI_13_Right','CI_14_Left','CI_14_Right','change_Left',"change_Right")

## c

fl=rbind(flights13[,c(10,13)],flights14[,c(9,12)])
group_f1=group_by(fl,carrier,origin)
f1_sum=summarize(group_f1,percent=n())
group_f2=group_by(fl,origin)
f2_sum=summarize(group_f2,count=n())
f1_sum=arrange(f1_sum,origin)
f1_sum$percent[1:12]=f1_sum$percent[1:12]/208235
f1_sum$percent[13:22]=f1_sum$percent[13:22]/192762
f1_sum$percent[23:36]=f1_sum$percent[23:36]/189095

fl_13_14=left_join(al13_at_least_0.01,f1_sum,by="carrier")
fl_13_14=fl_13_14[,-2]
fl_13_14=arrange(fl_13_14,origin)
fl_EWR=fl_13_14%>%filter(fl_13_14$origin=='EWR')
fl_JFK=fl_13_14%>%filter(fl_13_14$origin=='JFK')
fl_LGA=fl_13_14%>%filter(fl_13_14$origin=='LGA')
EWR=f_CI(fl_EWR$percent.y,208235,1,10)
JFK=f_CI(fl_JFK$percent.y,192762,1,9)
LGA=f_CI(fl_LGA$percent.y,189095,1,11)
ap_CI=rbind(EWR,JFK,LGA)
FL_13_14=cbind(fl_13_14,ap_CI)
###largest carrier at EWR
fl_13_14[which.max(fl_EWR$percent.y),1]
###largest carrier at JFK
fl_13_14[which.max(fl_JFK$percent.y),1]
###largest carrier at LGA
fl_13_14[which.max(fl_LGA$percent.y),1]
###table
colnames(FL_13_14)=c('carrier','airport','percent','CI_left','CI_right')


