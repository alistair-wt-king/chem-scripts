#DS determination of single substituents on cellulose by 31PNMR.
#Alistair W. T. King
# www.helsinki.fi/cellulose-chemistry
# see DOI: 10.1039/c0ay00336k


#Variables:
#Molecular weight of the substituent, from point of attachment to the cellulose oxygen atom (g/mol)
#Molarity of the internal standard (mMol)
#Volume of the internal standard (microL)
#integration ratio of free OHs to IS, by 31P-NMR
#The sample weight for analysis (mg)

print("Determination of DS of native or artifact lignocellulosics from 31P NMR\n\n")


#   DSvalue        free OH per weight    based on the molecular weight of the monomer unit (3/162)
#
#	0					18.52
#	1					12.35
#	2					6.173
#	3					0

y = 0.01852

#y is mol hydroxyls per gram of unsubstituted sample

FragMW1 = input("\n\nPlease enter the molecular weight of the substituent fragment\nDo not include the attaching oxygen\nIf the fragment has extra labile protons, devide the Molecular weight by\nthe number of extra labile protons\nIf there is no substituent, enter '1': ")

FragMW = FragMW1 - 1

#FragMW = corrected value for substraction of a hydrogen atom from available hydroxyls

ISmMol = input('\n\nEnter the internal standard molarity, in mmol/L: ')

#ISmMol has to be a float or a zero division error is returned as of python v 2.3

ISmMol= float(ISmMol)
    
#float(x) is required to avoid a python error. If x is already a float, it is simply returned unaltered

ISvol = input('\n\nEnter the volume of IS in the NMR sample, in microL: ')

#ISvol = internal standard volume

OHrat = input('\n\nEnter the total integration ratio of free HO to \ninternal standard integrals: ')

ISmol = ISmMol * ISvol / 1000000000

#ISmol = mols of internal standard in solution

FOHmol = ISmol * OHrat

#FOHmol = mols of free OH groups in the solution

Swt = input('\n\nEnter the weight of the sample that was analysed, in mg: ')

FOHpg = 1000 * FOHmol / Swt

#FOHpg = mols per gram based upon the 31P integration

mFOHpg =str(round(1000 * FOHpg, 4))

#mFOHpg = mmols of hydroxyls per gram, from 31P integration values to 4 decimals

FOHth = ((y/FOHpg) - 1)/(FragMW + (1/FOHpg))

#FOHth = quantitiy of hydroxyls that are taken up by substituent, in mmol/g

#the more condensed FOHth = y + y/FOHpg*FragMW - FOHpg - 1/FragMW gives a zero integer division error with python 2.3

DS = 3 * FOHth / y
psDS = 100 * FOHth / y

#DS = DS value
#psDS = % DS value

DS = str(round(DS, 3))

#value to 3 decimals

if FragMW1 == 1:
    totpsphos = str(round(100 - psDS, 2))
    # % of total theoretical (3/162) nuclei observed in solution to 2 decimals
    print("\n\n\nThe % phosphitylation is " + `totpsphos` + " % of the total theoretical value.\nThis can be an indication of either insolubility\nof the phosphitylated product or incomplete phosphitylation.\n\n")
    print("The integral region corresponds to a value of " + `mFOHpg` + " mmol/g\n\n")

else:
    print("\n\n\nThe degree of substitution is " + `DS` + "\n\n")