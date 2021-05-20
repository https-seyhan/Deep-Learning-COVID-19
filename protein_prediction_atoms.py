import os
import collections
import xpdb   # this is the module described below
import pandas as pd
import glob
from collections import Counter
from Bio.PDB import *

location = '/home/saul/protein/544698_993839_bundle_archive/structures_4_3_2020'
os.chdir(location)

sloppyparser = PDBParser(PERMISSIVE=True,
                         structure_builder=xpdb.SloppyStructureBuilder())
class Atoms:
    def __init__(self):
        self.atomlist= []
        self.PL_PRO_C_terminal = pd.DataFrame(columns=['Atom', 'freq'])
        self.nsp2 = pd.DataFrame(columns=['Atom', 'freq'])
        self.nsp4= pd.DataFrame(columns=['Atom', 'freq'])
        self.M_protein = pd.DataFrame(columns=['Atom', 'freq'])
        self.Protein_3a = pd.DataFrame(columns=['Atom', 'freq'])
        self.nsp6 = pd.DataFrame(columns=['Atom', 'freq'])
        self.pdbfile = ''
    def getPDB(self, filename):
        self.pdbfile = filename.split(".")[0]
        #print("File Name {} !!!".format(self.pdbfile))
        structure = sloppyparser.get_structure('MD_system', filename)
        self.atoms = structure.get_atoms()
        print("File name {} has atoms {}".format(filename, self.atoms))
        self.__atomdict()
    def getResidue(self):
        print("Residue")
    def __atomdict(self):
        print("atomdict called!!!")
        for atom in self.atoms:
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
        atomfreq = collections.Counter(atoms)
        sortedatomfreq = {k: v for k, v in sorted(atomfreq.items(), key=lambda item: item[1], reverse=True)}
        #print(sortedatomfreq)
        self.__printAtomFreq(sortedatomfreq, atomfreq)
    def __printAtomFreq(self, sortedatomfreq, atomfreq):
        # Print Atom frequency by descented order
        print("File Name {} !!!".format(self.pdbfile))
        for item, val in enumerate(sortedatomfreq):
            # print(" Item {} has the value of {}".format(item, val))
            print(" Atom {} has the value of {}".format(val, atomfreq[val]))
            # print(" Item {} has the value of {}".format(item, val))

            if self.pdbfile == 'PL_PRO_C_terminal':
                print("File {} called".format(self.pdbfile ))
                new_row = {'Atom': val, 'freq': atomfreq[val]}
                self.PL_PRO_C_terminal = self.PL_PRO_C_terminal.append(new_row, ignore_index=True, )
                

            elif self.pdbfile == 'nsp2':
                print("File {} called".format(self.pdbfile ))

            elif self.pdbfile == 'nsp4':
                print("File {} called".format(self.pdbfile ))

            elif self.pdbfile == 'nsp6':
                print("File {} called".format(self.pdbfile))

            elif self.pdbfile == 'M_protein':
                print("File {} called".format(self.pdbfile))

            elif self.pdbfile == 'Protein_3a':
                print("File {} called".format(self.pdbfile ))
            else:
                print("File does not exist")
        print("PDB file ", self.pdbfile)
        self.__outputPDB()

    def __getPDBData(self, val, freq, pdbname):
        new_row = {'Atom': val, 'freq': atomfreq[val]}
        self.pdbname= self.pdbname.append(new_row, ignore_index=True, )

    def __outputPDB(self):
        self.PL_PRO_C_terminal.to_csv('self.PL_PRO_C_terminal_freq.csv', sep=',', index=False)

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
