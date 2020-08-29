#Python script for determining proton affinities and gas-phase basicities from 2 orca thermochem output files by Alistair King
#Cartesian coordinates assumed for input files
#linear molecules with three or more atoms should be calculated by hand
# www.helsinki.fi/cellulose-chemistry

import sys
import os

#check for arguements

if len(sys.argv) != 2:
	print 'Usage: python protonaffinity-orca.py <folder> \n'
	print len(sys.argv)
	sys.exit(1)
	
folder = sys.argv[1]
folder = folder.rstrip('\\')
Acidfilename= str(folder) + '/protonated/orca.out'
Basefilename= str(folder) + '/base/orca.out'


#some constants

H2kcal = 627.53 # for conversion from Hartrees to kcals
T = 298.15 # Kelvin
R = 0.0019872 # kcal.mol-1.K-1


#################acid#####################
#open the file, copy as a string and close

Acidfile=open(Acidfilename)

Afilestring=Acidfile.read()

Acidfile.close()


#rfind to locate the last ENERGY COMPONENTS in the string

index = Afilestring.rfind('Final Gibbs free enthalpy', 1)

index = Afilestring.find('...', index)

AG = H2kcal*float(Afilestring[index+6:index+19])

index = Afilestring.rfind('Total Enthalpy', 1)

index = Afilestring.find('...', index)

AH = H2kcal*float(Afilestring[index+6:index+19])



#################base######################
#open the file, copy as a string and close

Basefile=open(Basefilename)

Bfilestring=Basefile.read()

Basefile.close()


#rfind to locate the last ENERGY COMPONENTS in the string

index = Bfilestring.rfind('Final Gibbs free enthalpy', 1)

index = Bfilestring.find('...', index)

BG = H2kcal*float(Bfilestring[index+6:index+19])

index = Bfilestring.rfind('Total Enthalpy', 1)

index = Bfilestring.find('...', index)

BH = H2kcal*float(Bfilestring[index+6:index+19])


#################proton######################


HH = 1.48 # 5/2 RT in kcal/mol at RT
HG = -6.28 # kcal/mol at RT, taken from Moser et al, DOI: 10.1021/jp107450n (Sackur-Tetrode derivation)


###############final calculation################


deltaH = HH + BH - AH

deltaG = HG + BG - AG

print "\n\nThe proton affinity is " + str(deltaH) + " kcal/mol\n\n"

print "The gas-phase basicity is " + str(deltaG) + " kcal/mol\n\n"
