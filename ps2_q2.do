cd E:\506
*import sasxport OHX_D.XPT,clear
*save OHX_D
*import sasxport DEMO_D.XPT,clear
*save DEMO_D
*clear

* a
** merge data
use DEMO_D.dta
merge 1:1 seqn using OHX_D.dta


* b
** delete the missing data
mvdecode ohx04htc, mv(9=.)
drop if missing(ohx04htc)

** change values into 1 and 0
replace ohx04htc=2 if ohx04htc==5
replace ohx04htc=0 if ohx04htc==2|ohx04htc==4

** do logistic regression
logit ohx04htc ridagemn

** get age of 25, 50, 75 percentile
gen age_25=round((log(0.25/0.75)-8.359362)/(-0.0696778))
gen age_50=round((log(0.5/0.5)-8.359362)/(-0.0696778))
gen age_75=round((log(0.75/0.25)-8.359362)/(-0.0696778))

** Choose a range of representative age values by taking the floor (in years) of 
** the 25%-ile and the ceiling (in years) of the 75%-ile.
gen year_75=ceil(age_25/12)
gen year_25=floor(age_75/12)
display(year_75)
display(year_25)

*** The range of ages is 8:12 (in year).


* c
** 1
logit ohx04htc ridagemn
estat ic
logit ohx04htc ridagemn i.riagendr
estat ic
*** We can see the BIC of this model is 1542.055, which is bigger than BIC of 
*** the model in part b(1533.407). So, we don't retain it.

** 2
*** create indicators of different categories:
replace ridreth1=2 if ridreth1==5
label define ridreth1 3 "NH White", 
label define ridreth1 4 "NH Black", add
label define ridreth1 1 "Mex American", add
label define ridreth1 2 "Other race/ethn", add

*** compare the BIC of the model before and after the addition of indicator 
*** Mexico American:
preserve
replace ridreth1=0 if ridreth1==2|ridreth1==3|ridreth1==4
logit ohx04htc ridagemn i.ridreth1
estat ic
*** The BIC of category American Mexico is 1542.285, 
*** which doesn't improve the last BIC(1533.407). So, we don't retain it.
restore

*** compare the BIC of the model before and after the addition of indicator 
*** Non-Hispanic Black:
preserve
replace ridreth1=0 if ridreth==1|ridreth==2|ridreth==3
replace ridreth1=1 if ridreth==4
logit ohx04htc ridagemn i.ridreth1
estat ic
*** The BIC of category Non-Hispanic Black is 1529.281, 
*** which improves the last BIC(1533.407). So, we retain it.
restore

*** compare the BIC of the model before and after the addition of indicator 
*** Other race/ethn:
preserve
replace ridreth1=0 if ridreth==1|ridreth==3|ridreth==4
replace ridreth1=1 if ridreth==2
logit ohx04htc ridagemn i.ridreth1
estat ic
*** The BIC of category Other is 1541.932, which doesn't improve 
*** the last BIC(1533.407). So, we don't retain it.
restore

** 3
*** We add the predictor for category Non-Hispanic Black
replace ridreth1=0 if ridreth==1|ridreth==2|ridreth==3
replace ridreth1=1 if ridreth==4
gen race_NH_black=ridreth1

*** compare the BIC before and after the addition of the variable poverty income ratio:
drop if missing(indfmpir)
logit ohx04htc ridagemn i.race_NH_black indfmpir
estat ic
*** The BIC of it with the addition variable poverty income ratio is 1462.895, 
*** which improves the last BIC(1529.281). So, we retain it.

*** Finalmodel: logit ohx04htc ~ ridagemn i.race_NH_black indfmpir ***


* d
*** change the age from month to year
gen age_year=trunc(ridagemn/12)

*** do logistic regression of the final model
quietly logit ohx04htc age_year i.race_NH_black indfmpir

** 1 Adjusted predctions at the mean (for other values) at each of the representative ages:
margins, at(age_year=(8(1)11)) atmeans
marginsplot

** 2
*** The marginal effects at the mean of variable race_NH_black at the same representative ages:
margins, at(age_year=(8(1)11)) dydx(race_NH_black) atmeans
marginsplot

*** The marginal effects at the mean of variable poverty income ratio at the same representative ages:
margins, at(age_year=(8(1)11)) dydx(indfmpir) atmeans
marginsplot

** 3
*** The average marginal effect of varialbal race_NH_black at the representative ages:
margins, at(age_year=(8(1)11)) dydx(race_NH_black)
marginsplot

*** The average marginal effect of varialbal poverty income ratio at the representative ages:
margins, at(age_year=(8(1)11)) dydx(indfmpir)
marginsplot


* e
*** Refit final model from part c using svy
svyset sdmvpsu [pweight=wtmec2yr],strata(sdmvstra) vce(linearized)
svy: logit ohx04htc age_year i.race_NH_black indfmpir
est store m2

logit ohx04htc age_year race_NH_black indfmpir
est store m1

*** We can tell from the two tables that the absolute value of the coefficients
*** of the svy model are smaller than that of the original final model.
*** Besides, the standard errors of svy model are bigger than that of the original final model.
*** In addition, the p-value of every coefficients of svy model are larger than that of the 
*** original final model.
*** Finally, the confidence intervals of svy model are longer than that of the original model.
