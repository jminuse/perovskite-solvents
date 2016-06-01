# code for packmol simulations


import os, sys, random, math, re, pickle
from merlin import *
import numpy

def run(run_name, solvent_name, solute=None, seed=1):
	
			
	extra = {  #(47, 3, 46):(85.00, 120.00), (47, 47, 3, 46):(0.0, 14.0, 0.0, 0.0),
		#Pb: utils.Struct(index=Pb, index2=Pb_, element_name='Pb', element=82, mass=207.2, charge=2.0, vdw_e=0., vdw_r=4.0),
		#Cl: utils.Struct(index=Cl, index2=Cl_, element_name='Cl', element=17, mass=35.45, charge=-0.0, vdw_e=0.01, vdw_r=4.0),
	}

	system = utils.System(box_size=(25, 25, 25), name=run_name)
	
	solvent=utils.Molecule('cml/'+solvent_name, extra_parameters=extra)
	
	if solute:
		solute = utils.Molecule('cml/'+solute, check_charges=False)
		system.add(solute)

	files.packmol(system, (solvent,), (1,), 0.7, seed)
	
	os.chdir('lammps')
	files.write_lammps_data(system,True)
	
	commands = ('''units real
atom_style full
pair_style lj/cut/coul/dsf 0.05 10.0 10.0
bond_style harmonic
angle_style harmonic
dihedral_style opls

boundary p p p
read_data	'''+run_name+'''.data

dump 1 all xyz 100 '''+run_name+'''.xyz

fix av all ave/time 1 1000 1000 c_thermo_pe
thermo_style custom f_av pe temp press
thermo 1000

group mobile id > '''+str(len(solute.atoms) if solute else 0)+'''
minimize 1.0e-4 1.0e-6 100 1000
velocity mobile create 300.0 '''+str(seed)+''' rot yes dist gaussian
fix motion mobile npt temp 300.0 300.0 100.0 aniso 1.0 1.0 1000.0
#fix motion mobile nvt temp 300.0 300.0 100.0
timestep 2.0
run 1000
write_restart '''+run_name+'''.restart''')

	open(run_name+'.in', 'w').write(commands)

	os.system('/fs/home/bas348/lammps/15May2015/src/lmp_serial -in '+run_name+'.in -log '+run_name+'.log')
	
	xyz = files.read_xyz(run_name+'.xyz')
	print len(xyz), 'frames'
	for a,b in zip(system.atoms,xyz[-1]):
		a.x, a.y, a.z = b.x, b.y, b.z
		if any( [numpy.isnan(x) for x in (a.x,a.y,a.z)] ):
			return None
	molecules_in_cluster = []

	if solute:
		pb = [a for a in system.atoms if a.element=='Pb'][0]
		for m in system.molecules:
			R = utils.dist(pb,m.atoms[0])
			molecules_in_cluster.append( (R,m) )
	else:
		origin = utils.Atom('X',0.0,0.0,0.0)
		for m in system.molecules:
			R = utils.dist(origin,m.atoms[0])
			molecules_in_cluster.append( (R,m) )

	molecules_in_cluster.sort()

	molecules_in_cluster = [m[1] for m in molecules_in_cluster[ : (11 if solute else 10) ]]#11 if solute else 10

	for m in molecules_in_cluster:
		for i,a in enumerate(m.atoms):
			a.index = i+1

	system = utils.System(box_size=(100, 100, 100), name=run_name+'_1')
	for m in molecules_in_cluster:
		system.add(m)
		for a,b in zip(system.molecules[-1].atoms, m.atoms):
			a.x, a.y, a.z = b.x, b.y, b.z
	files.write_lammps_data(system,True)
	
	commands = ('''units real
atom_style full
pair_style lj/cut/coul/dsf 0.05 10.0 10.0
bond_style harmonic
angle_style harmonic
dihedral_style opls

boundary p p p
read_data	'''+system.name+'''.data

dump 1 all xyz 100 '''+system.name+'''.xyz

fix av all ave/time 1 100 100 c_thermo_pe
thermo_style custom f_av pe temp press
thermo 100

group mobile id > '''+str(len(solute.atoms) if solute else 0)+'''
minimize 1.0e-4 1.0e-6 1000 10000
velocity mobile create 100.0 '''+str(seed)+''' rot yes dist gaussian
#fix motion mobile npt temp 300.0 300.0 100.0 aniso 1.0 1.0 1000.0
fix motion mobile nvt temp 100.0 100.0 100.0
run 1000
minimize 1.0e-4 1.0e-6 1000 10000

write_restart '''+system.name+'''.restart''')

	open(system.name+'.in', 'w').write(commands)

	os.system('/fs/home/bas348/lammps/15May2015/src/lmp_serial -in '+system.name+'.in -log '+system.name+'.log')

	xyz = files.read_xyz(system.name+'.xyz')
	print len(xyz), 'frames'
	for a,b in zip(system.atoms,xyz[-1]):
		a.x, a.y, a.z = b.x, b.y, b.z
		if any( [numpy.isnan(x) for x in (a.x,a.y,a.z)] ):
			return None
	files.write_xyz(system.atoms, run_name+'.cluster')	
	pickle.dump(system, open(run_name+'.pickle', 'w'))

	os.chdir('..')

	dielectrics = dict( zip(['benzene','odcb','nitromethane'], [2.27,9.93,35.87]) )
	extra_section='%%cosmo  SMD true  epsilon %f  end' % dielectrics[solvent_name]
	orca.job(run_name, '! OPT B97-D3 SV GCP(DFT/SV) ECP{def2-TZVP} COSMO Grid3 FinalGrid5 SlowConv LooseOpt', system.atoms, queue='batch', mem=50, extra_section=extra_section, charge=2 if solute else 0)


#run(sys.argv[1], sys.argv[2], None if sys.argv[3]=='None' else sys.argv[3], int(sys.argv[4]) )

for i in range(20):
	for solvent in ['benzene','odcb','nitromethane']: #'methacrolein', 'gbl','ACN', 'DMF','dmso','nmp', 'acetone'
		for solute in ['pb2+', 'None']:
			name = '%s_%s_%d' % (solute, solvent, i)
			run(name, solvent, None if solute=='None' else solute, seed=i+1)
