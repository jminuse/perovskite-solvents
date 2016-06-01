	#g09.job('dbl_acetone_Cl_3', 'HSEH1PBE/LanL2DZ Opt  SCF=QC SCRF(Solvent=Acetone) guess=read geom=(check,newdefinition)',queue='long' ,previous='dbl_acetone_Cl_2')
def opt1():
	for h in ['Cl', 'I']:
		frames= files.read_xyz('xyz/%s.xyz'%h)
		for solv in ['1,2-EthaneDiol']:
			g09.job('%s_%s_Def_S'%(h,solv.replace('-','_').replace(',','_')),'HSEH1PBE/def2SVP  SCRF(Solvent=%s)'%solv, atoms=frames, queue='batch', force=True, charge_and_multiplicity='-1,1')

def opt2():
	for old_job in []:
		atoms = g09.atoms(old_job)
		new_job=old_job+'_Def_S'
		for solv in ['1,2-EthaneDiol']:
			g09.job(new_job, '%s_%s_Def_S'%(h,solv.replace('-','_').replace(',','_')), 'HSEH1PBE/Def2SVP OPT SCRF(Solvent=1,2-EthaneDiol) guess=read geom=(check,newdefinition)', queue= 'long')




def solv():
	g09.job('dbl_buty_I1_4', 'HSEH1PBE/LanL2DZ OPT SCF=XQC SCRF(Solvent=1,2-EthaneDiol) guess=read geom=(check,newdefinition)',  queue= 'long',previous='dbl_buty_I1_3')




def mbs_Inew():
# optimization using MBS from a previous job using single BS-the folllowing is for PbI2
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

def mbs_clnew():
	# optimization using MBS from a previous job using single BS-the folllowing is for PbCl2
	for old_job in []:
		atoms = g09.atoms(old_job)

		elements = [a.element for a in atoms]

		if 'H' in elements and 'Cl' in elements:
			g09.job(old_job+'_Cmbs', 'HSEH1PBE/GenECP Opt SCRF(Solvent=Acetone)', atoms=atoms, queue='batch', extra_section='''H C O Cl 0\ncc-pVDZ\n****
		Pb 0\nSDD\n****

		Pb 0\nSDD\n\n''')
		elif 'Pb' in elements:
			g09.job(old_job+'_Cmbs', 'HSEH1PBE/GenECP Opt SCRF(Solvent=Acetone)', atoms=atoms, queue='batch', extra_section='''Cl 0\ncc-pVDZ\n****
		Pb 0\nSDD\n****

		Pb 0\nSDD\n\n''')
		else:
			g09.job(old_job+'_Cmbs', 'HSEH1PBE/cc-pVDZ Opt SCRF(Solvent=Acetone)', atoms=atoms, queue='batch')


def Imbs():
	# optimization with implicit solvent for MBS from xyz file- below id for I
	frames=files.read_xyz('xyz/dbl_buty_Cl.xyz')

	route = 'SP SCRF(Solvent=Acetone) guess=read SCF=QC'

	g09.job('dblI_Cmbs', 'HSEH1PBE/GenECP '+route, atoms=frames, queue='batch', extra_section='''H C O 0\ncc-pVDZ\n****
		Pb 0\nSDD\n****
		I 0\nDef2TZVP\n****

		Pb 0\nSDD\n\n''')


def Cmbs():
	#optimization with implict solvent for MBS from XYZ file-below is for Cl
	frames=files.read_xyz('.xyz')

	route = 'SP SCRF(Solvent=Acetone) guess=read SCF=QC'

	g09.job('dblI_Cmbs', 'HSEH1PBE/GenECP '+route, atoms=frames, queue='batch', extra_section=
	'''H C O Cl 0\ncc-pVDZ\n****
	Pb 0\nSDD\n****


	Pb 0\nSDD\n\n''')

def restart_mbs():
	# to restart jon using mixed basis set from previous job
	g09.job('pbi2_4acetone_8_Imbs', 'HSEH1PBE/chkbasis Opt SCRF(Solvent=Acetone) SCF=QC geom=(check,newdefinition)', queue='long', previous='pbi2_4acetone_7_Imbs')

def halide():
	for old_job in ['pbi2_solv_ACN','pbi2_1acetoN_4','pbi2_2acetoN_6','pbi2_3acetoN_42','4ACN_s_4','pbcl2_solv_ACN','pbcl2_1acetoN_4','pbcl2_2acetoN_6','pbcl2_3acetoN_43','4ACN_s_4_pbcl2']:
		atoms=g09.atoms(old_job)
		halide=[a for a in atoms if a.element in['Cl','I']]
		#print len(atoms)
		for h in halide:
			i=atoms.index(h)
			atoms=atoms[:i] +atoms[i+1:]
		new_job=old_job+'_Def_S_2+'
		#print len(atoms)
		g09.job(new_job, 'HSEH1PBE/Def2SVP Opt SCRF(Solvent=Acetonitrile)', atoms=atoms, queue='long', force=True, charge_and_multiplicity='2,1')