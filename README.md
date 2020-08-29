# chem-scripts
A bunch of very simple scripts for processing computational and other specific chemical data, relevant to our research: https://www.helsinki.fi/cellulose-chemistry.

These are typically for extracting computational outputs and doing some simple data processing.
There is no real interaction between these scripts, except for concat-scanenergies-terachem.py, which will read the outputs from bondlength_energies-kcal-terachem.py and concatenate them into a csv. This allows for a more rapid construction of relaxed potential energy surface scans in excel for graphing.

boltzmannfactor.py - is a Python script for calculating the Boltzmann factor of a structure. Requested energies are in kcal/mol. Temperatures are in Kelvin. Output     will allow for the relative population of an geometry, compared to another. 0 kcal/mol will give a value of 1.

ktparams.py - is a Python script for determination of Kamlet-Taft parameters from the UV absorption maxima of the typical 3 dyes that are used for analysis of ionic liquids - diethylnitroaniline, nitroaniline and Reichardt's dye.

bondlength_energies-kcal-terachem - is a Python script for outputting energies (in kcals) for a bondlengthscan in Terachem.

concat-scanenergies-terachem.py - is a Python 3 script for concatenating energies to a csv for a bondlengthscans potential energy surfaces in Terachem.

elementalDS-cellulose.py - is a Python 2 script for DS calculation based on microanalysis.

geoope_energies-terachem.py - is a Python 2 Script for outputting energies for a geometry optimisation in Terachem.

neb_energies-terachem.py - is a Python 2 Script for outputting energies from NEB xyz frames in Terachem.

phosphorous_cellulose.py - is a Python 2 script for DS determination of single substituents on cellulose by 31PNMR, according to DOI: 10.1039/c0ay00336k

protonaffinity-orca.py - is a Python 2 script for determining proton affinities and gas-phase basicities from 2 orca thermochem output files.

xyz-extract-gamess.py - is a Python 2 script for extracting the final geometries in xyz format (xyz - Å) from gamess MP2 thermochem outputs (cartesian - AU).
