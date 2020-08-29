#Determination of Kamlet-Taft parameters from UV absorptions by Alistair W. T. King
# www.helsinki.fi/cellulose-chemistry


LBDmaxRD = float(input('\n\nEnter the LAMBDAmax for the Reichardts Dye solution in nm: '))
LBDmaxNA = float(input('\n\nEnter the LAMBDAmax for the 4-NitroAniline solution in nm: '))
LBDmaxDENA = float(input('\n\nEnter the LAMBDAmax for the N,N-Diethyl-4-NitroAniline solution in nm: '))

NUmaxRD = 1 / (LBDmaxRD * 0.0001)
NUmaxNA = 1 / (LBDmaxNA * 0.0001)
NUmaxDENA = 1 / (LBDmaxDENA * 0.0001)

ET30 = 28592 / LBDmaxRD

PIst = 0.314 * (27.52 - NUmaxDENA)

ALPHA = 0.0649 * ET30 - 2.03 - (0.72 * PIst)

BETA = (1.035 * NUmaxDENA + 2.64 - NUmaxNA) / 2.8


print("\n\n\nALPHA = " + `ALPHA` + " \n\nBETA = " + `BETA` + " \n\nPI* = " + `PIst` + " \n\nET(30) = " + `ET30` + " \n\n")