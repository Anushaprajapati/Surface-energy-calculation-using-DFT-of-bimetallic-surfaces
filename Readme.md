Installation
1. Python version 'Python 3.11.7'
 Packages ASE and ACAT
2. Softwares
a. CP2K - to perform DFT calculations.
b. VMD - to visualize, manipulate and save metallic structures in desired format.
c. ASE GUI - to visualize, manipulate and save metallic structures in desired format.

USAGE
Steps to find surface energies of desired metallic surfaces
1. Generating bimetallic structures
   
This repository has 3 files cp2k_input.inp, get_structures.py and mpi_slurm_cp2k.sh
1.01 make a directory for each pair compostion of Au-Pt bimetallic surfaces.

1.02. Each directory should contain the above 3 files.

1.03. Open the get_structures.py python file and enter the composition of Au-Pt structure and run the python script using 'python get_structures.py' command in the command prompt.

1.04. Once the python script runs, open the pdb file and note the coordinates and include it in the cp2k_input.inp file which should be in base directory under the directory created for each compositions. 

1.05. the generated structures can be moves to files directory under the main directory.

1.06 To run cp2k, 'nohup ./mpi_slurm_cp2k.sh  files/ &' and enter in the command prompt.

1.07. The cp2k calculation can be tracked using 'top' command, and 'jobs' command can be used to check it's status(running, done, exit, etc).

1.08. After the calculation in completed, a list of directories gets saved in the main directory, with each directory having the list of files au0.1pt0.9-RESTART.wfn  au0.1pt0.9-RESTART.wfn.bak-1  cp2k.inp  cp2k.out 

1.09. The cp2.out file contains the energy value.

1.10. Calculate the energy value for all surfaces and bulk and the surface energy value can be calculated using the formula, Surface energy =
((Energy of surface) −( Number of atoms in surface×Energy of bulk×Number of atoms bulk))/(2 × Surface area).

1.11. Number of atoms in the bulk and surface can be noted from the pdb file, and the surface area is the product of a and c coordinates of the structure.


 
