from Bio.PDB import *
import os
import collections
location = '/home/saul/protein/544698_993839_bundle_archive/structures_4_3_2020'
os.chdir(location)
import xpdb   # this is the module described below
import pandas as pd
from collections import Counter
from itertools import groupby
import glob # The glob module finds all the pathnames matching a specified pattern according to the rule

# parse protein structures
sloppyparser = PDBParser(PERMISSIVE=True,
                         structure_builder=xpdb.SloppyStructureBuilder())
structure = sloppyparser.get_structure('MD_system', 'M_protein.pdb')

atoms = structure.get_atoms()
lt = 0
atomlist = []

# collect COVID-19 atoms
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

# Print Atom frequency by descented order

for item, val in enumerate(sortedatomfreq):
    #print(" Item {} has the value of {}".format(item, val))
    print(" Atom {} has the value of {}".format(val, atomfreq[val]))
    #print(" Item {} has the value of {}".format(item, val))


def getFileNames(location):
    files = []
    print('getFileNames called!!!')
    #print(location)
    for file_name in glob.iglob(location + '/*.pdb', recursive=True):
        #print(file_name)
        #print(file_name.split('/')[-1])
        files.append(file_name.split('/')[-1])
    return  files

if __name__ == '__main__':
    fileNames = getFileNames(location)
    print(fileNames)



