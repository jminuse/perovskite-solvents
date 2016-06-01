import sys, os, copy
sys.path.append('/fs/home/jms875/Library')
import gaussian, filetypes

def job(atoms, name, previous_job=None):
	
	route = 'SP SCRF(Solvent=Acetone) guess=read SCF=QC'
	i = 1
	while os.path.isfile('gaussian/'+name+'.log'):
		name = name[:-1] + str(i)
		i = i+1
	gaussian.job(atoms, 'HSEH1PBE/LANL2DZ', 'long', name, route, previous=previous_job)
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

#binding_energy_dz('4ACN_s_4_pbcl2', 'pbcl2_3acetoN_43', 'ACN_solv', range (21))

binding_energy_dz('5_acetone_5_PbCl2', 'pbcl2_4acetone_3', 'acetone_1', range (43))


for job in []:
	 print job,gaussian.parse_atoms(job)[0]
	



