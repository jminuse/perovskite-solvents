from merlin import *

for old_job in []:
	atoms = g09.atoms(old_job)

	elements = [a.element for a in atoms]

	if 'H' in elements and 'Cl' in elements:
		g09.job(old_job+'_Cmbs', 'HSEH1PBE/GenECP Opt SCRF(Solvent=Acetone)', atoms=atoms, queue='batch' extra_section='''H C O Cl 0\ncc-pVDZ\n****
	Pb 0\nSDD\n****

	Pb 0\nSDD\n\n''')
	elif 'Pb' in elements:
		g09.job(old_job+'_Cmbs', 'HSEH1PBE/GenECP Opt SCRF(Solvent=Acetone)', atoms=atoms, queue='batch' extra_section='''Cl 0\ncc-pVDZ\n****
	Pb 0\nSDD\n****

	Pb 0\nSDD\n\n''')
	else:
		g09.job(old_job+'_Cmbs', 'HSEH1PBE/cc-pVDZ Opt SCRF(Solvent=Acetone)' atoms=atoms, queue='batch')

















	
