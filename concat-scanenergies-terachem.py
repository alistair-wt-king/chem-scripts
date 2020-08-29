# Python3 script for concatenating energies to a csv for a bondlengthscans potential energy surfaces in Terachem by Alistair W. T. King
# www.helsinki.fi/cellulose-chemistry

import sys
import csv
import os
import pandas as pd

#check for arguements

if len(sys.argv) < 2:
	print ('Usage: python bondlengthenergies-terachem.py <folder 1> <folder 2> ....\n')
	print (len(sys.argv))
	sys.exit(1)

n = len(sys.argv)

comb =[]

for i in range(1, n):
	arg_name = sys.argv[i]
	arg_name = arg_name.rstrip('\\')
	path = str(arg_name) + '/scr/scanenergiesxy.txt'
	comb.append(pd.read_csv(path))
	
combined_csv = pd.concat(comb, ignore_index=True)
	
combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

with open('combined_csv.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('combined_csv.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Bond Length (Angstroms)','00','01','2.5','05','10','20','30','40','50','60','70','80'])
    w.writerows(data)
