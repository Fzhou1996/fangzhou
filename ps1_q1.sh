# !/bin/bash
# q1
# Part A
# I 
cut -d'', -f2 recs2015_public_v3.csv| grep 3| wc -l
# II
cut -d'', -f1, 475:571 recs2015_public_v3.csv


# Part B
# I
for i in {1..4}
do
cut -d'', -f2 recs2015_public_v3.csv|grep $i| wc -l
done

# II
cut -d'', -f2,3 recs2015_public_v3.csv|sort|uniq > region_division.txt

