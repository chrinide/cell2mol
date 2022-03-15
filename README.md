cell2mol: Unit Cell to Molecule Interpretation
==============================================

![cell2mol logo](./images/cell2mol_logo.png)

## Contents
* [About](#about-)
* [Install](#install-)
* [Examples](#examples-)
* [Errors](#errors-)

## About [↑](#about)

Program that interprets .cif files of molecular crystals and retrieves structural, connectivity and charge information of all molecules present in the unit cell. This includes (but is not limited to):

- Atomic coordinates, labels
- Total molecular charge, and formal atomic charges, including metal oxidation states
- Connectivity network as defined by either the adjacency matrix or the bond-order matrix 

The program generates a so-called "cell" object, with hierarchical information on the unit cell. "Cells" have "Molecules". Molecules that hold a transition metal are considered a "Complex". Complexes are made of "Ligands" and "Metals". "Ligands" are made of "Groups" of connected "Atoms". 

"Complexes", "Ligands", "Metals" and "Groups" host the information of their constituent "Atoms". That way, cell2mol provides a very in-depth interpretation of unit cells, which can be particularly useful to generate controlled databases for Quantum Chemistry and Machine Learning applications. 

The code runs on pure python with minimal dependencies: 
- `numpy`
- `scipy`
- `pandas`
- `networkx`
- `RDkit` 

## Install [↑](#install)

Download and add c2m_driver.py to your path. No strings attached. Run as:

```python
python c2m_driver.py [-h] -i FILENAME [-s STEP]
```

You can also execute:

```python 
python setup.py install
```

to install cell2mol as a python module. Afterwards, you can call cell2mol as:

```python 
python -m cell2mol [-h] -i FILENAME [-s STEP]
```

which is the recommended way. Options can be consulted using the `-h` flag in either case.

## Examples [↑](#examples)

The test/infodata subdirectory contains a copious amount of tests which double as examples. Any of the .cif files can be run as:

```python
python -m cell2mol -i [FILENAME]
```

An output file will be created locally. Additionally, a .gmol file containing the analyzed unit cell will be written by cell2mol. The cell object contains all the information following the class specifications, and can be loaded using the pickle library for further usage.

As a reference, cell2mol characterizes the crystal structure of "YOXKUS" (available in the test/infodata directory) as follows: YOXKUS has 4 Re complexes and no counterion or solvent molecules. Each complex has 3 types of ligands. The first ligand bears a -1 charge, and is connected to the Rh ion through two groups of atoms. The first group consists of a substituted Cp ring with η5 hapticity, and the other is the P atom of a diphenylphosphine, with κ1 denticity. The second ligand is an iodine atom with -1 charge, and appears twice. The third is a neutral CO ligand, with a -1 and a +1 formal charge in the C and O atoms, respectively, and a triple bond between them.

## Errors [↑](#errors)

There are a few legitimate limitations and errors in algorithms of cell2mol.

1.	In cell2mol, an atom has a neutral charge and the number of electrons in an atom is equal to the atomic number of an element. Also, valence electrons should participate in forming chemical bonds while satisfying the octet rule. Therefore, errors happen when interpreting the intrinsically negative charged species: counterions such as triiodide ion I<sub>3</sub><sup>-</sup> and azide ion N<sub>3</sub><sup>-</sup>, and radical anion ligands. 
2.	Ligands with multiple resonance structures sometimes have more than one plausible charge interpretation by cell2mol. Specifically, aromatic ligands with heteroatoms often have multiple resonance structures, which results in either a neutral or negative charge of the ligand.
3.	Every metal-ligand coordination bond is regarded as a single bond in cell2mol, so interpretation for metal-ligand multiple bonding does not work. A typical example is a metal-carbene complex containing metal-carbon double or triple bonds. cell2mol cannot identify the exact bond order between a metal and a carbon atom and the resulting charge of the carbene ligand.
4.	A nitrosyl (NO) ligand has a different charge depending on its geometry: a linear NO with 0 charge, while a bent NO with -1 charge. Although cell2mol determines the NO ligand geometry by calculating the M(metal)-N-O angle, this characteristic of NO ligands may cause the discrepancy between the cell2mol interpretation and the metal oxidation state reported in .cif file. 

---
