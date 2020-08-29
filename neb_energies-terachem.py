#Python 2 Script for outputting energies from NEB xyz frames in Terachem by Alistair King
#No arguments required..just type 'python neb_energies.py'
# www.helsinki.fi/cellulose-chemistry

import matplotlib.pyplot as plt
import glob

#obtain the file names in the directory

list_of_files = glob.glob('./neb_*.xyz')

#create lists for sorting of the file names

sorted_list_of_integers =[]

sorted_list_of_files =[]

#sort the file list to a list of integers

for file_name in list_of_files:
	stripped = file_name.lstrip('./neb_')
	stripped = stripped.rstrip('.xyz')
	sorted_list_of_integers.append(int(stripped))

sorted_list_of_integers.sort()

#convert back to the file names

for file_name in sorted_list_of_integers:
	concat = './neb_' + str(file_name) + '.xyz'
	print concat
	sorted_list_of_files.append(concat)

#create lists for the x and y components..file name and energy

energ = []
name = []

#create a new output file for the xy data

FO = open('nebenergiesxy.xy','w') 

#extract the energies for each file and write to the lists

for file_name in sorted_list_of_files:
	FI = open(file_name, 'r')
	string = FI.read()
	text = string[3:26]
	energ.append(text)
	stripped = file_name.lstrip('./neb_')
	stripped = stripped.rstrip('.xyz')
	name.append(stripped)
	FI.close()
	FO.write(text)
	FO.write(',')
	FO.write(stripped)
	FO.write('\n')

FO.close()

#plot and save the image

plt.plot(name, energ, 'ro-')
plt.ylabel('Energy (Hartree)')
plt.xlabel('NEB Image')
plt.tight_layout()

plt.savefig('NEBenergies.png')
plt.show()
