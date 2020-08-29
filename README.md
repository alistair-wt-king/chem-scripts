# chem-scripts
A bunch of scripts for processing computational and other chemical data.

These are typically for extracting computational outputs and doing some simple data processing.
There is no real interaction between these scripts, except for concat-scanenergies-terachem.py, which will read the outputs from bondlength_energies-kcal-terachem.py and concatenate them into a csv. This allows for a more rapid construction of relaxed potential energy surface scans in excel for graphing.

boltzmannfactor.py - is a Python script for calculating the Boltzmann factor of a structure. Requested energies are in kcal/mol. Temperatures are in Kelvin. Output will allow for the relative population of an geometry, compared to another. 0 kcal/mol will give a value of 1.

ktparams.py - is a Python script for determination of Kamlet-Taft parameters from the UV absorption maxima of the typical 3 dyes that are used for analysis of ionic liquids - diethylnitroaniline, nitroaniline and Reichardt's dye.

Python script for outputting energies (in kcals) for a bondlengthscan in Terachem
