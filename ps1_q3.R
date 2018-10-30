# Q3
recs2015<-read.csv("E:/506/recs2015_public_v3.csv")
library(dplyr)

## a
wall=recs2015%>%filter(recs2015$WALLTYPE==4)
group_wall=group_by(wall,DIVISION)
h=matrix(nrow=10,ncol=96)
wall_sum=summarize(group_wall,homes=sum(NWEIGHT))
group_division=group_by(recs2015,DIVISION)
division_sum=summarize(group_division,homes=sum(NWEIGHT))
div_stucco=transmute(wall_sum,division=DIVISION,percent=wall_sum$homes/division_sum$homes)
### highest porportion
div_stucco[which.max(div_stucco$percent),1]
### lowest porportion
div_stucco[which.min(div_stucco$percent),1]
### standard error
### For 2015 Recs,R=96,e=0.5


### b
### average KWH
group_elec=group_by(recs2015,DIVISION)
elec_sum=summarize(group_elec,total=sum(KWH*NWEIGHT),average=total/sum(NWEIGHT))

### average KWH stratified by urban and rural status
Recs_UR=recs2015%>%filter(recs2015$UATYP10!='C')
group_elec_UR=group_by(Recs_UR,DIVISION,UATYP10)
elec_UR_sum=summarize(group_elec_UR,average=sum(KWH*NWEIGHT)/sum(NWEIGHT))


### c
###
Recs_IT=Recs_UR%>%filter(Recs_UR$INTERNET==1)
group_IT=group_by(Recs_IT,DIVISION,UATYP10)
IT_sum=summarize(group_IT,homes=sum(NWEIGHT))
UR_sum=summarize(group_elec_UR,homes=sum(NWEIGHT))
UR_IT=data.frame(IT_sum,c(IT_sum$homes/UR_sum$homes))
UR_IT=UR_IT[,-3]
colnames(UR_IT)=c('division','urbantype','proportion')
disp=c()
for (i in 1:10){disp[i]=UR_IT$proportion[2*i]-UR_IT$proportion[2*i-1]}
### Division with largest disparity between urban and rural areas 
which.max(abs(disp))


