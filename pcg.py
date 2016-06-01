import sys, os, copy
sys.path.append('/fs/home/jms875/Library/2.0/tools')
import g09, utils

for old_job in['acetone_1_Imbs']:
	atoms = g09.atoms(old_job)
	
	#g09.job(old_job+'_HTg', 'HSEH1PBE/LANL2DZ SCRF(Solvent=Acetone) Pop=HLYGAt geom=check guess=read', previous=old_job)
	charges=g09.parse_chelpg('gaussian/'+old_job+'_HTg.log')
	
	

	for atom, charge in zip(atoms,charges):
		atom.charge=charge
		if "O" ==atom.element:
			print old_job,charge
	










