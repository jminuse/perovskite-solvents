import os, copy, sys, random, cPickle, math
sys.path.append("/fs/home/jms875/build/lammps/lammps-15May15/python")
from lammps import lammps
sys.path.append("/fs/home/jms875/Library/2.0")
import utils, files

system = utils.System(box_size=(30., 30., 30.), name='test4')

THF = utils.Molecule('cml/THF')

molecules = [THF]
molecule_ratio = [1]
density = 0.889

files.packmol(system, molecules, molecule_ratio, density)

os.chdir('lammps')
files.write_lammps_data(system)

commands = ('''units real
atom_style full
pair_style lj/cut/coul/long 10.0
bond_style harmonic
angle_style harmonic
dihedral_style opls
special_bonds lj/coul 0.0 0.0 0.5

read_data	'''+system.name+'''.data
kspace_style pppm 1.0e-4

thermo_style custom density tpcpu
thermo 100
dump 1 all xyz 100 '''+system.name+'''.xyz
minimize 1.0e-4 1.0e-6 100 1000

fix 1 all npt temp 300.0 300.0 100.0 iso 1.0 1.0 1000.0
velocity all create 300.0 1 rot yes dist gaussian
run 10000
''').splitlines()
lmp = lammps()
for line in commands:
	lmp.command(line)

os.chdir('..')

