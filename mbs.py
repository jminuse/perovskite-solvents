from merlin import *
# optimization using MBS from a previous job using single BS
for old_job in [pbi2_4acetone_3_Imbs]:
	atoms = g09.atoms(old_job)

	

	elements = [a.element for a in atoms]

	if 'H' in elements and 'I' in elements:
		g09.job(old_job+'_Imbs', 'HSEH1PBE/GenECP Opt SCRF(Solvent= Acetone)', atoms=atoms, queue='batch', extra_section='''H C O 0\ncc-pVDZ\n****
	Pb 0\nSDD\n****
	I 0\nDef2TZVP\n****

	Pb 0\nSDD
	I 0\nDef2TZVP\n\n''')
	elif 'Pb' in elements:
		g09.job(old_job+'_Imbs', 'HSEH1PBE/GenECP Opt SCRF(Solvent= Acetone)', atoms=atoms, queue='batch', extra_section='''Pb 0\nSDD\n****
	I 0\nDef2TZVP\n****

	Pb 0\nSDD
	I 0\nDef2TZVP\n\n''')
	else:
		g09.job(old_job+'_Imbs', 'HSEH1PBE/cc-pVDZ Opt SCRF(Solvent= Acetone)', atoms=atoms, queue='batch')
	
















