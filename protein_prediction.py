from Bio.PDB import *
import os
os.chdir('/home/saul/protein/544698_993839_bundle_archive/structures_4_3_2020')
import xpdb   # this is the module described below
import pandas as pd
from collections import Counter

from itertools import groupby

# read
sloppyparser = PDBParser(PERMISSIVE=True,
                         structure_builder=xpdb.SloppyStructureBuilder())
structure = sloppyparser.get_structure('MD_system', 'M_protein.pdb')

atoms = structure.get_atoms()
lt = 0
atomlist = []

for atom in atoms:
    #print(type(atom))
    lt = lt + 1
    atomlist.append(atom)

#print(Counter(atomlist))

atomdict = Counter(atomlist)

print(atomdict)
for item, val in enumerate(atomdict):
   print(" Item {} has the value of {}".format(item, val))

atomdist = [len(list(group)) for key, group in groupby(atomlist)]
#print(atomdist)
#print(atomlist)