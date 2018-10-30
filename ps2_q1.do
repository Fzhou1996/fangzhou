cd E:\506
set more off
* import delimited recs2015_public_v3.csv
* save recs2015_public_v3.dta
* clear
use recs2015_public_v3.dta,clear


* 1. Total electricity usage in kilowatt hours
generate total_kwh=kwh*nweight
egen sum_kwh0=sum(total_kwh)

*** write a loop to get standard error
foreach i of num 1/96{
generate t`i'=brrwt`i'*kwh
egen sum_kwh`i'=sum(t`i')
generate std`i'=(sum_kwh`i'-sum_kwh0)^2
}
egen a=rowtotal(std1-std96)
gen std_error_kwh=(a/24)^(1/2)

preserve
keep sum_kwh0 std_error_kwh
restore


* 2. Total natural gas usage, in hundreds of cubic feet

generate total_cufeet=cufeetng*nweight
egen sum_cufeet0=sum(total_cufeet)

*** standard error
foreach i of num 1/96{
generate u`i'=brrwt`i'*cufeetng
egen sum_cufeet`i'=sum(u`i')
generate std_`i'=(sum_cufeet`i'-sum_cufeet0)^2
}
egen b =rowtotal(std_1-std_96)
gen std_error_cufeet=(b/24)^(1/2)

preserve
keep sum_cufeet0 std_error_cufeet
restore


* 3. Propane usage, in gallons

generate total_gallonlp=gallonlp*nweight
egen sum_lp0=sum(total_gallonlp)

*** get standard error
foreach i of num 1/96{
generate p`i'=brrwt`i'*gallonlp
egen sum_lp`i'=sum(p`i')
generate std_lp`i'=(sum_lp`i'-sum_lp0)^2
}
egen c =rowtotal(std_lp1-std_lp96)
gen std_error_lp=(c/24)^(1/2)

preserve
keep sum_lp0 std_error_lp
restore


* 4. Fuel oil or kerosene usage, in gallons

generate total_gallonfo=gallonfo*nweight
egen sum_fo0=sum(total_gallonfo)

*** get standard error
foreach i of num 1/96{
generate f`i'=brrwt`i'*gallonfo
egen sum_fo`i'=sum(f`i')
generate std_fo`i'=(sum_fo`i'-sum_fo0)^2
}
egen d =rowtotal(std_fo1-std_fo96)
gen std_error_fo=(d/24)^(1/2)

preserve
keep sum_fo0 std_error_fo
restore

*** export these variables to excel
collapse (mean)sum_kwh0 std_error_kwh sum_cufeet0 std_error_cufeet sum_lp0 std_error_lp sum_fo0 std_error_fo
export delimited recs2015_usage.csv
