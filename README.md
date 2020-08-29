# chem-scripts
A bunch of scripts for processing computational and other chemical data.

These are typically for extracting computational outputs and doing some simple data processing.
There is no real interaction between these scripts, except for concat-scanenergies-terachem.py, which will read the outputs from bondlength_energies-kcal-terachem.py and concatenate them into a csv. This allows for a more rapid construction of relaxed potential energy surface scans in excel for graphing.

boltzmanfactor.py is a Python script for calculating the Boltzmann factor of a structure. Requested energies are in kcal/mol. Temperatures are in Kelvin. Output will allow for the relative population of an geometry, compared to another. 0 kcal/mol will give a value of 1.


