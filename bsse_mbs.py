
import sys, os, copy
sys.path.append('/fs/home/jms875/Library')
import gaussian, filetypes

def job(atoms, name, previous_job=None):
	
	route = 'SP SCRF(Solvent=Butanal) SCF=(QC,maxcycles=2000)'
	i = 1
	while os.path.isfile('gaussian/'+name+'.log'):
		name = name[:-1] + str(i)
		i = i+1

	elements = [a.element.replace('-Bq', '') for a in atoms]
	
	

	if 'H' in elements and 'I' in elements:
		gaussian.job(atoms, 'HSEH1PBE/GenECP', 'batch', name, route, previous=previous_job, extra_section='''H C O 0\ncc-pVDZ\n****
Pb 0\nSDD\n****
I 0\nDef2TZVP\n****

Pb 0\nSDD
I 0\nDef2TZVP\n\n''')
	elif 'Pb' in elements:
		gaussian.job(atoms, 'HSEH1PBE/GenECP', 'batch', name, route, previous=previous_job, extra_section='''Pb 0\nSDD\n****
I 0\nDef2TZVP\n****

Pb 0\nSDD
I 0\nDef2TZVP\n\n''')
	else:
		gaussian.job(atoms, 'HSEH1PBE/cc-pVDZ', 'batch', name, route, previous=previous_job)
	return name

def binding_energy_dz(job_total, job_A, job_B, zero_indexed_atom_indices_A):
	AB = gaussian.atoms(job_total)
	AB_A = copy.deepcopy(AB)
	for i,atom in enumerate(AB_A):
		if i not in zero_indexed_atom_indices_A: atom.element+='-Bq'
	AB_B = copy.deepcopy(AB)
	for i,atom in enumerate(AB_B):
		if i in zero_indexed_atom_indices_A: atom.element+='-Bq'
	#now AB_A is A from AB, AB_B is B from AB
	name1 = job(AB_A, job_total+'_A0', previous_job=job_total)
	name2 = job(AB_B, job_total+'_B0', previous_job=job_total)
	
	#non-rigid correction:
	AB_A = [atom for atom in AB_A if not atom.element.endswith('-Bq')]
	AB_B = [atom for atom in AB_B if not atom.element.endswith('-Bq')]
	name3 = job(AB_A, job_A+'_AB0', previous_job=job_A)
	name4 = job(AB_B, job_B+'_AB0'+('2' if job_A==job_B else ''), previous_job=job_B)
	
	print 'E_binding = %s - %s - %s + %s + %s - %s - %s' % (job_total, name1, name2, name3, name4, job_A, job_B)

#binding_energy_dz('pbi2_6methc_9_Imbs', 'pbi2_5methc_12_Imbs', 'methc_solv_Imbs', range (58))

#binding_energy_dz('pbcl2_3acetone_3_Cmbs', 'pbcl2_2acetone_5_Cmbs', 'acetone_1_Cmbs', range (10,23))


for job in ['pbi2_6methc_9_Imbs','pbi2_6methc_9_Imbs_A0','pbi2_6methc_9_Imbs_B0','pbi2_5methc_12_Imbs_AB0','methc_solv_Imbs_AB4','pbi2_5methc_12_Imbs','methc_solv_Imbs']:
	 print job,gaussian.parse_atoms(job)[0]