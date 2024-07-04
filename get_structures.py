#!/usr/bin/env python

from acat.build.ordering import RandomOrderingGenerator as ROG
from ase.build import bulk
from ase.io import read, write
from ase.visualize import view



structure  = bulk('Pt',crystalstructure = 'fcc', a=4, orthorhombic=True)
bulkstructure = structure * (7, 7, 7)
rog = ROG(bulkstructure, elements=['Pt', 'Au'],
          composition={'Pt': 1, 'Au': 0})

rog.run(num_gen=30, unique=True)
images = read('orderings.traj', index=':')
# view(images)  # Uncomment this line if you want to visualize the images

# Write each configuration to a separate XYZ file
for i, image in enumerate(images):
    # Swap Y and Z coordinates
    for atom in image:
        atom.position[1], atom.position[2] = atom.position[2], atom.position[1]

    cell_params = image.get_cell_lengths_and_angles()
    cell_line = f"{cell_params[0]:.6f} {cell_params[2]:.6f} {cell_params[1]:.6f} {cell_params[3]:.6f} {cell_params[5]:.6f} {cell_params[4]:.6f}\n"

    
   # Write the image to an XYZ file with cell parameters in the header
    with open(f'ordering_{i+1}.xyz', 'w') as outfile:
        # Write cell parameters as comment line
        outfile.write(f"{len(image)}\n")
        outfile.write(f"Cell parameters: {cell_line}")
        
        # Write atom coordinates
        for atom in image:
            element = atom.symbol
            x, y, z = atom.position
            outfile.write(f"{element} {x:.6f} {y:.6f} {z:.6f}\n")



