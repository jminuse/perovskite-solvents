from merlin import *

def opt_o1(): # double zeta for solutes, triple zeta for lead, read from xyz file, zips solute with apporpriate charge
	solutes=[ 'pbcl','pbcl2', 'pbcl3', 'pbcl_ma','pbcl2_ma','pbcl3_ma']
	charges=[1,0,-1,2,1,0]
	for name,charge in zip(solutes, charges):
		atoms=files.read_xyz('xyz/%s.xyz'%name)
		orca.job(name,'! OPT B97-D3 def2-SVP ECP{def2-TZVP}', atoms, charge_and_multiplicity='%d 1'%charge, queue= 'batch')

def opt_o2(): # double zeta set on individual solvent molecules, zips solvent with appropraite dielectric
	names=['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']
	dielectrics=[20.7, 37.5, 36.7, 46.7, 40.24, 10.9 ,32.2]
	for name,dielectric in zip(names, dielectrics):
		atoms = utils.Molecule('SMRFF/cml/'+name, parameter_file=None).atoms
		orca.job(name, '! OPT B97-D3 COSMO def2-SVP', atoms,  queue='batch', extra_section='%%cosmo  SMD true  epsilon %f  end' % dielectric)

def opt_o3(): # sinlge point calculation on individual solvents, zips dielectric with solvent
	names=['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']
	dielectrics=[20.7, 37.5, 36.7, 46.7, 40.24, 10.9 ,32.2]
	for name,dielectric in zip(names, dielectrics):
		orca.job(name+'_1', '! RIJCOSX RI-PWPB95 COSMO D3BJ Def2-QZVPP(-g,-f) ECP{def2-TZVP} TIGHTSCF Grid5 FinalGrid6 SlowConv',  queue='batch', extra_section='%%cosmo  SMD true  epsilon %f  end' % dielectric, previous=name)

def sp_pb_only(): # quad zeta on lead atom in vacumn
		atoms=[ utils.Atom('Pb',0,0,0) ]
		orca.job('pb2+_vac.4.1', '! RIJCOSX RI-PWPB95 D3BJ Def2-QZVPP(-g,-f) ECP{def2-TZVP}  SlowConv', atoms, queue=None, charge_and_multiplicity='2 1')#TIGHTSCF Grid5 FinalGrid6

def sp_pb_only_TZ(): # triple  zeta on lead atom in vacumn
		atoms=[ utils.Atom('Pb',0,0,0) ]
		orca.job('pb2+_vac.3', '! B97-D3 def2-TZVP ECP{def2-TZVP} Grid3 FinalGrid5 SlowConv', atoms, queue=None, charge_and_multiplicity='2 1')



def opt_o4(): # triple zeta on individual solvent molecules
	names=['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']
	dielectrics=[20.7, 37.5, 36.7, 46.7, 40.24, 10.9 ,32.2]
	for name,dielectric in zip(names, dielectrics):
		orca.job(name+'_TZ', '! OPT B97-D3 def2-TZVP GCP(DFT/TZ) ECP{def2-TZVP} COSMO Grid3 FinalGrid5 SlowConv',  queue='batch', extra_section='%%cosmo  SMD true  epsilon %f  end' % dielectric, previous=name)

def opt_o5(): # single point calculation on individual solvent molecules
	names=['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']
	dielectrics=[20.7, 37.5, 36.7, 46.7, 40.24, 10.9 ,32.2]
	for name,dielectric in zip(names, dielectrics):
		extra_section='%%cosmo  SMD true  epsilon %f  end' % dielectric
		orca.job(name+'_.4', '! RIJCOSX RI-PWPB95 D3BJ Def2-QZVPP(-g,-f) ECP{def2-TZVP} TIGHTSCF Grid5 FinalGrid6 SlowConv', previous=name, queue='batch', mem=1500, extra_section=extra_section, charge_and_multiplicity='0 1')

def opt_6(): # double zeta read from xyz file, zips solute with apporpriate charge
	names=['dimer_3_3_anti']
	dielectrics=[36.7]#40.24,20.7,46.7,36.7,10.9,37.5
	for name,dielectric in zip(names, dielectrics):
		atoms=files.read_xyz('xyz/%s.xyz'%name)
		orca.job(name+'_dz','! OPT B97-D3 def2-sVP GCP(DFT/TZ) ECP{def2-TZVP}', atoms, queue= 'medium',extra_section='%%cosmo  SMD true  epsilon %f  end' % dielectric)










def opt_dimer_dz(): # geometry optimizations for 2 pbcl3MA with dmso solvents from xyz files double zeta
	names=['dimer_3_3_anti']#'monomer_1dmso','monomer_2dmso','monomer_3dmso','monomer_4dmso','monomer_5dmso' 'dimer_4_4_anti','dimer_4_3_anti','dimer_3_3_anti','dimer_3_2_anti','dimer_4_4','dimer_4_3','dimer_3_3','dimer_3_2'  
	for name in names:
		atoms = files.read_xyz('xyz/%s.xyz'%name)
		orca.job(name+'_eb_dz', '! Opt B97-D3 def2-sVP GCP(DFT/TZ) ECP{def2-TZVP} COSMO printbasis', atoms, queue='medium', extra_section='%cosmo  SMD true  solvent "DMSO" end \n%basis aux auto NewECP Pb "def2-SD" "def2-TZVP" end NewGTO S "def2-TZVP" end end')


def opt_restart_dz(): #  triple zeta geometery opt pbcl3ma from previous double zeta
	old_name=['dimer_4_4_anti_eb_dz']
	for name in old_name:
		new_name=name[:-3]+'_dz_2'
		orca.job(new_name, '! Opt B97-D3 def2-sVP GCP(DFT/TZ) ECP{def2-TZVP} COSMO printbasis', previous=name, queue='medium', extra_section='%cosmo  SMD true  solvent "DMSO" end \n%basis aux auto NewECP Pb "def2-SD" "def2-TZVP" end NewGTO S "def2-TZVP" end end')		

def opt_dimer_tz(): #  triple zeta geometery opt pbcl3ma from previous double zeta
	old_name=['monomer_4dmso_sq_dz']
	for name in old_name:
		new_name=name[:-3]+'_tz'
		orca.job(new_name, '! Opt B97-D3 def2-TZVP GCP(DFT/TZ) ECP{def2-TZVP} COSMO printbasis', previous=name,queue='medium', extra_section='%cosmo  SMD true  end')

def opt_dimer_dh(): #  triple zeta geometery opt pbcl3ma from previous double zeta
	old_name=['pass_monomer_tz']
	for name in old_name:
		new_name=name[:-3]+'_dh'
		orca.job(new_name, '! RIJCOSX RI-PWPB95 D3BJ Def2-QZVPP(-g,-f) ECP{def2-TZVP} COSMO printbasis', previous=name,queue='medium', extra_section='%cosmo  SMD true  end')



def opt_dimer_1(): # geometry optimizations for 2 pbcl3MA with dmso solvents triple zeta
	names=['2pbcl3ma_apart_5dmso_opt', '2pbcl3ma_joined_5dmso_opt', '2pbcl3ma_joined_5dmso_2_opt'] #['2pbcl3ma_p_opt', '2pbcl3ma_opt', '2pbcl3ma_4dmso_p_opt', '2pbcl3ma_3dmso_p_opt', '2pbcl3ma_2dmso_p_opt', '2pbcl3ma_1dmso_p_opt', '2pbcl3ma_4dmso_opt', '2pbcl3ma_3dmso_opt', '2pbcl3ma_2dmso_opt', '2pbcl3ma_1dmso_opt','2pbcl3ma_apart_5dmso_opt', '2pbcl3ma_joined_5dmso_opt', '2pbcl3ma_joined_5dmso_2_opt']
	for name in names:
		atoms = orca.read('/fs/home/jms875/build/lammps/lammps-7Dec15/src/test/orca/%s/%s.out'%(name,name)).atoms
		previous = '/fs/home/jms875/build/lammps/lammps-7Dec15/src/test/orca/%s/%s.orca.gbw'%(name,name)
		orca.job(name, '! Opt B97-D3 def2-TZVP GCP(DFT/TZ) ECP{def2-TZVP} COSMO printbasis', atoms, queue='debug', previous=previous,  extra_section='%cosmo  SMD true  solvent "DMSO"  end\n%basis aux auto NewECP Pb "def2-SD" "def2-TZVP" end NewGTO S "def2-TZVP" end end')

def opt_odd_solvent(): 
	old_name=['nitmeth_opt']
	for name in old_name:
		new_name=name[:-3]+'_dh'
		orca.job(new_name, '! RIJCOSX RI-PWPB95 D3BJ Def2-QZVPP(-g,-f) ECP{def2-TZVP} COSMO printbasis',previous=name, queue='medium', extra_section='%%cosmo  SMD true  epsilon %f  end' )











def test_memory_options(): # quad zeta on lead atom in vacumn
		previous = 'None_acetone.5_0'
		for memory in ['DOUBLE', 'CDOUBLE', 'CFLOAT']:
			orca.job('acetone_'+memory.lower(), '! RIJCOSX RI-PWPB95 D3BJ Def2-QZVPP(-g,-f) ECP{def2-TZVP} '+memory, queue=None, previous=previous, extra_section='%scf maxiter 0 end')

def test_maxiter_0(): #fine, easy to calculate final energy from MP2+SCF
	for digit,extra in enumerate(['%scf maxiter 0 end', '']):
		orca.job('pb2+_test_maxiter_%d'%digit, '! RIJCOSX RI-PWPB95 D3BJ Def2-QZVPP(-g,-f) ECP{def2-TZVP}', queue=None, charge_and_multiplicity='2 1', previous='pb2+_vac.4.1', extra_section=extra)

def text_auxiliary_basis(): #fine, default auxiliary basis sets are the same
	#def2-TZVP def2-TZVP/JK def2-TZVP/C
	orca.job('pb2+_test_auxiliary', '! RIJCOSX RI-PWPB95 D3BJ Def2-QZVPP(-g,-f) QZVPP/JK QZVPP/C ECP{def2-TZVP}', queue=None, charge_and_multiplicity='2 1', previous='pb2+_vac.4.1').wait() 

def benzene_guess():
	benzene = files.read_xyz('xyz/benzene')
	atoms = []
	atoms.append( utils.Atom('Pb', -10, 0, 0) )
	import copy
	for i in range(8):
		for a in copy.deepcopy(benzene):
			a.x += 10.0*i
			atoms.append(a)
	files.write_xyz(atoms, 'xyz/pb_8benzene')

def pb_benzene(): # triple  zeta on lead atom in vacumn
	atoms=files.read_xyz('xyz/pb_8benzene')
	orca.job('pb2+_benzene.3', '! B97-D3 def2-SVP GCP(DFT/SVP) ECP{def2-TZVP} Grid3 FinalGrid5  SlowConv LooseOpt', atoms, queue='medium', procs=4, charge_and_multiplicity='2 1')

def pb_benzene_1(): #  triple zeta geometery opt pbcl3ma from previous double zeta
	names=['pb2+_benzene.3']
	for name in names:
		atoms=orca.read(name).atoms
		orca.job(name+'_dz','! B97-D3 def2-SVP GCP(DFT/SVP) ECP{def2-TZVP} Grid3 FinalGrid5  SlowConv LooseOpt', atoms, queue='medium', procs=4, charge_and_multiplicity='2 1')

def sp_pb_pure_dft_gcp(): # triple  zeta on lead atom in vacumn
	atoms=[ utils.Atom('Pb',0,0,0) ]
	orca.job('pb2+_vac_b97d_tz_gcp', '! B97-D3 def2-TZVP GCP(DFT/TZ) ECP{def2-TZVP} Grid3 FinalGrid5 SlowConv', atoms, queue=None, charge_and_multiplicity='2 1')

sp_pb_pure_dft_gcp()
