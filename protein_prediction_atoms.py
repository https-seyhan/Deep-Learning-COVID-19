from Bio.PDB import *
import os
import collections
location = '/home/saul/protein/544698_993839_bundle_archive/structures_4_3_2020'
os.chdir(location)
import xpdb   # this is the module described below
import pandas as pd
from collections import Counter
from itertools import groupby
import glob

# read
sloppyparser = PDBParser(PERMISSIVE=True,
                         structure_builder=xpdb.SloppyStructureBuilder())


class Atoms:

    def __init__(self):

        self.atomlist= []
        self.PL_PRO_C_terminal = pd.DataFrame()
        self.nsp2 = pd.DataFrame()
        self.nsp4= pd.DataFrame()
        self.M_protein = pd.DataFrame()
        self.Protein_3a = pd.DataFrame()
        self.nsp6 = pd.DataFrame()
        self.pdbfile = ''


    def getPDB(self, filename):
        self.pdbfile = filename
        structure = sloppyparser.get_structure('MD_system', filename)
        self.atoms = structure.get_atoms()
        print("File name {} has atoms {}".format(filename, self.atoms))
        self.__atomdict()
    def __atomdict(self):
        print("atomdict called!!!")
        for atom in self.atoms:
            # print(type(atom))
            self.atomlist.append(atom)
        atomdict = Counter(self.atomlist)
        #print(atomdict)
        self.__atomfreq(atomdict)

    def __atomfreq(self, atomdict):
        atoms = []
        for item, val in enumerate(atomdict):
            # print(" Item {} has the value of {}".format(item, val))
            value = str(val).strip('<>Atom ')
            atoms.append(value)
            # print(value)
            atoms.append(value)

        atomfreq = collections.Counter(atoms)
        sortedatomfreq = {k: v for k, v in sorted(atomfreq.items(), key=lambda item: item[1], reverse=True)}
        #print(sortedatomfreq)
        self.__printAtomFreq(sortedatomfreq, atomfreq)

    def __printAtomFreq(self, sortedatomfreq, atomfreq):
        # Print Atom frequency by descented order

        for item, val in enumerate(sortedatomfreq):
            # print(" Item {} has the value of {}".format(item, val))
            print(" Atom {} has the value of {}".format(val, atomfreq[val]))
            # print(" Item {} has the value of {}".format(item, val))

            if self.pdbfile == 'PL_PRO_C_terminal':
                print("This is it")
                self.PL_PRO_C_terminal.columns = ['Atom', 'freq']

            elif self.pdbfile == 'nsp2':
                self.nsp2.columns = ['Atom', 'freq']

            elif self.pdbfile == 'nsp4':
                self.nsp4.columns = ['Atom', 'freq']

            elif self.pdbfile == 'nsp6':
                self.nsp4.columns = ['Atom', 'freq']

            elif self.pdbfile == 'M_protein':
                self.M_protein.columns = ['Atom', 'freq']

            elif self.pdbfile == 'Protein_3a':
                self.Protein_3a.columns = ['Atom', 'freq']
            else:
                print("File does not exist")


        print("PDB file ", self.pdbfile)


def getFileNames(location):
    files = []
    print('getFileNames called!!!')
    #print(location)
    for file_name in glob.iglob(location + '/*.pdb', recursive=True):
        #print(file_name)
        #print(file_name.split('/')[-1])
        files.append(file_name.split('/')[-1])
    return files

if __name__ == '__main__':
    proteins= Atoms()
    #proteins.atomdict()
    fileNames = getFileNames(location)
    #print(fileNames)
    for name in range(len(fileNames)):
        print(fileNames[name])
        proteins.getPDB(fileNames[name])









