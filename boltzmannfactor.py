#Python script for calculating the Boltzmann factor of a structure by Alistair W. T. King
# www.helsinki.fi/cellulose-chemistry

import sys

#check for arguments

if len(sys.argv) != 3:
	print '\n\nUsage: python boltzmannfactor.py energy (kcal/mol), temperature (Kelvin)\n\nUse 298 for RT'
	print len(sys.argv)
	sys.exit(1)

# retrieve arguments

E=float(sys.argv[1])
T=float(sys.argv[2])

print sys.argv[1]
print sys.argv[2]

#some constants

invBC = 503.22 # inverse of Boltzmann Constant in K/kcal

e = 2.71828 # Euler's number

#calculate the Boltzmann factor

BF = e**(-E*invBC/T)

print "\nThe Boltzmann Factor is " + str(BF) + " \n"
