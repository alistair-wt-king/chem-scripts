#Python 2 Script for outputting energies for a geometry optimisation in Terachem by Alistair King
#No arguments required..just type 'python geoopt_energies-terachem.py'
# www.helsinki.fi/cellulose-chemistry

import sys
import matplotlib.pyplot as plt
	
#Open the file and read each line to a list, then close file

file = open('optim.xyz')

list = []

for line in file: 
        line = line.strip()
        list.append(line)
        
file.close()

#create two lists for the x and y values (bond length and energy)

xlist = []

ylist = []

#create a file for the comma separated values

output = open('optenergiesxy.xy','w')

#search and extract the energies and bond lengths from the list
#then write them to file and the new lists..then close file

for item in list:
	if item.find('frame') != -1:
		index = item.find('frame')
		text = item[index+6:index+10]
		text.strip()
		output.write(text)
		output.write(',')
		ylist.append(text)
		print str(text)
		text = item[index-24:index-11]
		output.write(text)
		output.write('\n')
		xlist.append(text)
		print str(text)	
			
output.close()

#plot the x & y values...then save an image

plt.plot(ylist, xlist, 'ro-')
plt.ylabel('Energy (Hartree)')
plt.xlabel('Frame')
plt.tight_layout()

plt.savefig('optenergies.png')
plt.show()
