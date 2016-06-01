import sys, os, copy
sys.path.append('/fs/home/jms875/Library/2.0/tools')
import g09, utils

for old_job in['pbi2opt_1']:
	atoms = g09.atoms(old_job)
	
	g09.job(old_job+'_HLYGAt', 'HSEH1PBE/LANL2DZ SCRF(Solvent= Acetone) Pop=HLYGAt geom=check guess=read', previous=old_job)

	#charges=g09.parse_chelpg('gaussian/'+old_job+'_Ht.log')
	
	#for a in atoms:
		#if a.element=='Pb':
			#Pb = a


	#for atom, charge in zip(atoms,charges):
		#atom.charge=charge
		#if "O" ==atom.element:
			#print old_job, utils.dist(Pb,atom),charge