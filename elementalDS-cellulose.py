#Python 2 script for DS calculation based on microanalysis by Alistair W. T. King
# www.helsinki.fi/cellulose-chemistry

#Atom types to be concidered are C, H, O, N, S
#Further atoms should be included and allowed to be inputed along with their accurate molecular weights

#the periodic table atom name, mean molecular weight values are stored in a dictionary
pt = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.0067, 'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.3050, 'Si': 28.0855, 'P': 30.973762, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078, 'Sc': 44.955912, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045, 'Fe': 55.845, 'Co': 58.933195, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723, 'Ge': 72.64, 'As': 74.92160, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Zr': 91.224, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98, 'Ru': 101.07, 'Rh': 102.90550, 'Pd': 106.42, 'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.710, 'Sb': 121.760, 'Te': 127.60, 'I': 126.90447, 'Xe': 131.293, 'Cs': 132.9054519, 'Ba': 137.327, 'La': 138.90547, 'Ce': 140.116, 'Pr': 140.907652, 'Nd': 144.2423, 'Pm': 145, 'Sm': 150.362, 'Eu': 151.9641, 'Gd': 157.253, 'Tb': 158.925352, 'Dy': 162.5001, 'Ho': 164.930322, 'Er': 167.2593, 'Tm': 168.934212, 'Yb': 173.043, 'Lu': 174.9671, 'Hf': 178.492, 'Ta': 180.947882, 'W': 183.841, 'Re': 186.2071, 'Os': 190.233, 'Ir': 192.2173, 'Pt': 195.0849, 'Au': 196.9665694, 'Hg': 200.592, 'Tl': 204.38332, 'Pb': 207.21, 'Bi': 208.980401, 'Po': 209, 'At': 210, 'Rn': 222, 'Fr': 223, 'Ra': 226, 'Ac': 227, 'Th': 232.038062, 'Pa': 231.035882, 'U': 238.028913, 'Np': 237, 'Pu': 244, 'Am': 243, 'Cm': 247, 'Bk': 247, 'Cf': 251, 'Es': 252, 'Fm': 257, 'Md': 258, 'No': 259, 'Lr': 262, 'Rf': 261, 'Db': 262, 'Sg': 266, 'Bh': 264, 'Hs': 277, 'Mt': 268, 'Ds': 281, 'Rg': 272, 'Uub': 285, 'Uut': 284, 'Uuq': 289, 'Uup': 288, 'Uuh': 291, 'Uuo': 294}

print "\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\nDetermination of DS1 from previously unsubstituted cellulose.\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\nPlease follow the prompts:\n\n"

#the next statement
#define a function DScalc for C, H, O, N, S

DS1v = {'C': 6, 'H': 10, 'O': 5}

print"\n\n@@@@@@@@@@@@@@@@@@\n\nYou will be now asked to enter the molecular formula of the substituent fragment, when prompted with the atom, please enter the number of atoms in the fragment formula. \n\n@@@@@@@@@@@@@@@@@@\n\n"
    
#FCas = number of atoms in the fragment forumla
FCas = input("\n\nCarbon. If none, enter 0: ")
FHas = input("\n\nHydrogen. If none, enter 0: ")
FOas = input("\n\nOxygen. If none, enter 0: ")
FNas = input("\n\nNitrogen. If none, enter 0: ")
FSas = input("\n\nSulfur. If none, enter 0: ")


def DScalc(DS1v):
    
    #Caa = number of carbon atoms in the starting molecule
    #Cma = mass of carbon, as from the periodic table dictionary

    Caa = DS1v.get('C')
    Cma = pt.get('C')
    Oaa = DS1v.get('O')
    Oma = pt.get('O')
    Haa = DS1v.get('H')
    Naa = 0
    Saa = 0
    
    Hma = pt.get('H')
    Nma = pt.get('N')
    Sma = pt.get('S')
    
    #Cpca = carbon percentage in molecule a (cellulose)
    Cpca = 100*Caa*Cma/(Caa*Cma+Oaa*Oma+Haa*Hma)
    Opca = 100*Oaa*Oma/(Caa*Cma+Oaa*Oma+Haa*Hma)
    Hpca = 100*Haa*Hma/(Caa*Cma+Oaa*Oma+Haa*Hma)
    Npca = 0
    Spca = 0


    #in order to correct gradient change attributed to increasing mass, dictionaries are created to recieve iterated key-value pairs of DS & percentage up to DS=15. This can then be looped through to find the lowest error fit. A value of 15 is used do determine the excess water in the sample and hopefully extrapolate a new DS value for the heavier atoms based on the excess hydrogen and oxygen weight attributed to excess water.

    print"Working....."
    CDSitdict = {}
    HDSitdict = {}
    ODSitdict = {}
    NDSitdict = {}
    SDSitdict = {}

    #Cwmax = maximum weight of carbon atoms, based on DS value of DSit

    DSit = 0
    while DSit < 4.0:
        Cwmax = Cma*(DSit*FCas+Caa)
        Hwmax = Hma*(DSit*FHas-DSit)+Hma*Haa
        Owmax = Oma*(DSit*FOas+Oaa)
        Nwmax = Nma*(DSit*FNas+Naa)
        Swmax = Sma*(DSit*FSas+Saa)

        Totalmaxwt = Cwmax+Hwmax+Owmax+Nwmax+Swmax
        Cpcmax = 100*Cwmax/Totalmaxwt
        Hpcmax = 100*Hwmax/Totalmaxwt
        Opcmax = 100*Owmax/Totalmaxwt
        Npcmax = 100*Nwmax/Totalmaxwt
        Spcmax = 100*Swmax/Totalmaxwt

        itera = "\'" + `DSit` + "\'"
        CDSitdict[itera] = Cpcmax
        HDSitdict[itera] = Hpcmax
        ODSitdict[itera] = Opcmax
        NDSitdict[itera] = Npcmax
        SDSitdict[itera] = Spcmax

        DSit += 0.00005

    Cwmax = Cma*(DSit*FCas+Caa)
    Hwmax = Hma*(DSit*FHas-DSit)+Hma*Haa
    Owmax = Oma*(DSit*FOas+Oaa)
    Nwmax = Nma*(DSit*FNas+Naa)
    Swmax = Sma*(DSit*FSas+Saa)

    Totalmaxwt = Cwmax+Hwmax+Owmax+Nwmax+Swmax
    Cpcmax = 100*Cwmax/Totalmaxwt
    Hpcmax = 100*Hwmax/Totalmaxwt
    Opcmax = 100*Owmax/Totalmaxwt
    Npcmax = 100*Nwmax/Totalmaxwt
    Spcmax = 100*Swmax/Totalmaxwt

    Cdiff = Cpcmax-Cpca
    Hdiff = Hpcmax-Hpca
    Odiff = Opcmax-Opca
    Ndiff = Npcmax-Npca
    Sdiff = Spcmax-Spca

    
    def pcloop(dictionary, exvalue):
        # Get a iterator over *both* keys and values.
        diter = dictionary.iteritems()

        # Get the first (key, value) pair.
        try:
            u, z = diter.next()

        except StopIteration:
            # The dictionary was empty!
            # You might want to do something else here
            return
        closest = abs(z - exvalue)
        result = u
        for u, z in diter:
            v = abs(z - exvalue)
            if v < closest:
                closest = v
                result = u

        return result

    #function defined to return the DS value. Excess DS is quoted as excess and 0 percent returns a DS of zero. This is required as the samples often contain water thus increasing the Hydrogen percentage.

    #pca = cellulose atom percentage
    #diff = percentage atom weight difference between DS=0 and DS=3
    #pcb = percentage value from the microanalysis for each atom type. if 0 is entered DS will be returned as 0
    #pcmax = DS=3 percentage for each atom type
    #wmax = DS=3 atom monomer weight
    #DS = DS value
    #atom.....

    def pcerror(pca, diff, pcb, pcmax, wmax, DS, atom):
        print"\n\nCellulose " + atom + " Percentage is " + `pca` + "\n\nMaximum potential monomer " +  atom + " weight is " + `wmax` + "\n\nMaximum potential " +  atom + " percentage is " + `pcmax` + "\n\nPercentage difference between Cellulose and Maximum (DS=3) is " + `diff` + "\n\n"
        if pcb < 0.001:
            print"\nThe DS value cannot be determined if the substrate contains no " + atom + "\n\n"
        elif diff < 0 and pca < pcb:
            print"There is excess " + atom + " in the sample."
        elif DS > 3:
            print"The calculated DS value is " + `DS` + "There is excess " + atom + " in the sample."
        else:
            print"\nThe calculated DS value based on the " + atom + " content is " + `DS` + "\n\n"
        return

    Cpcb = input("\n\nPlease enter the carbon percentage value obtained from the microanalysis: ")
    atom = 'carbon'
    CDS = pcloop(CDSitdict, Cpcb)
    print CDSitdict
    pcerror(Cpca, Cdiff, Cpcb, Cpcmax, Cwmax, CDS, atom)

    Hpcb = input("\n\nPlease enter the hydrogen percentage value obtained from the microanalysis: ")
    atom = 'hydrogen'
    HDS = pcloop(HDSitdict, Hpcb)
    pcerror(Hpca, Hdiff, Hpcb, Hpcmax, Hwmax, HDS, atom)
    
    Opcb = input("\n\nPlease enter the oxygen percentage value obtained from the microanalysis: ")
    atom = 'oxygen'
    ODS = pcloop(ODSitdict, Opcb)
    pcerror(Opca, Odiff, Opcb, Opcmax, Owmax, ODS, atom)
    
    Npcb = input("\n\nPlease enter the nitrogen percentage value obtained from the microanalysis. If none, enter 0: ")
    atom = 'nitrogen'
    NDS = pcloop(NDSitdict, Npcb)
    pcerror(Npca, Ndiff, Npcb, Npcmax, Nwmax, NDS, atom)
    
    Spcb = input("\n\nPlease enter the sulfur percentage value obtained from the microanalysis. If none, enter 0: ")
    atom = 'sulfur'
    SDS = pcloop(SDSitdict, Spcb)
    pcerror(Spca, Sdiff, Spcb, Spcmax, Swmax, SDS, atom)
  
    
DScalc(DS1v)
