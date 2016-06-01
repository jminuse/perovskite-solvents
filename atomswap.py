from merlin import *

for old_job in ['dbl_methc_Cl.xyz']:
	atoms= files.read_xyz('xyz/'+old_job)
	#atoms = g09.atoms(old_job)
	for a in atoms:
		if a.element=='Cl':
			a.element='I'
	
	#new_job=old_job+'_PbI2'
	new_job = old_job.replace('Cl', 'I').replace('.xyz', '') 
	g09.job(new_job, 'HSEH1PBE/LanL2DZ Opt SCRF(Solvent=Butanal)', atoms=atoms, queue='long', force=True)
