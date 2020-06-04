from Bio.PDB import *
import os
import collections
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
    atomlist.append(atom)

atomdict = Counter(atomlist)

atoms = []
for item, val in enumerate(atomdict):
   #print(" Item {} has the value of {}".format(item, val))
   value = str(val).strip('<>Atom ')
   atoms.append(value)
   #print(value)
   atoms.append(value)

atomfreq=collections.Counter(atoms)
#print(atomfreq)

sortedatomfreq = {k: v for k, v in sorted(atomfreq.items(), key=lambda item: item[1], reverse=True)}

#Print Atom frequency by descented order

for item, val in enumerate(sortedatomfreq):
    #print(" Item {} has the value of {}".format(item, val))
    print(" Atom {} has the value of {}".format(val, atomfreq[val]))
    #print(" Item {} has the value of {}".format(item, val))




