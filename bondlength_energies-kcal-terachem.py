#Script for outputting energies (in kcals) for a bondlengthscan in Terachem by Alistair W. T. King
# www.helsinki.fi/cellulose-chemistry

import sys
import matplotlib.pyplot as plt

#check for arguements

if len(sys.argv) != 2:
	print 'Usage: python bondlengthenergies.py <geometry.xyz> \n'
	print len(sys.argv)
	sys.exit(1)
	
#Open the file and read each line to a list, then close file

filename=sys.argv[1]

file=open(filename)

list = []

for line in file: 
        line = line.strip()
        list.append(line)
        
file.close()

#create two lists for the x and y values (bond length and energy)

xlist = []

ylist = []

yminlist = []

#create a file for the comma separated values

output = open('scanenergiesxy.txt','w')

#search and extract the energies and find the minimum value

for item in list:
	index = item.find('Converged')
	while index == 0:
		index = item.find('Energy')
		text = item[index+7:index+30]
#		print text
		yminlist.append(text)

ymin = max(yminlist)

ymin = float(ymin)

#for item in yminlist:
#	item = float(item) - float(ymin)
#	print item

#search and extract the energies and bond lengths from the list
#then write them to file and the new lists..then close file

for item in list:
	index = item.find('Converged')
	while index == 0:
		index = item.find('Energy')
		text = item[index+34:index+42]
#		print text
		output.write(text)
		output.write(',')
		xlist.append(text)
		text = item[index+7:index+30]
		text = float(text)
		text = text - ymin
		text = text * 627.509
		text = str(text)
#		print text
		output.write(text)
		output.write('\n')
		ylist.append(text)	
			
print ylist

output.close()



#plot the x & y values...then save an image

plt.plot(xlist, ylist, 'ro-')
plt.ylabel('Energy (kcal/mol)')
plt.xlabel('Bond Length (Angstrom)')
plt.tight_layout()

plt.savefig('scanenergies.png')
plt.show()
