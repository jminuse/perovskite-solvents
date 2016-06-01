# reads packmol .cluster files, and uses them as starting point geometries in orca for optimizations. 




from merlin import *

for i in range(0,50):
	for solvent,dielectric in zip(['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp'], [20.7, 37.5, 36.7, 46.7, 40.24, 10.9 ,32.2],):
		for solute in ['None', 'pb2+']:
			#extra_section='%%geom TolE=%f TolRMSG=%f TolMaxG=%f TolRMSD=%f TolMaxD=%f end\n%%cosmo  SMD true  epsilon %f  end' % tuple( [tol*100 for tol in (1e-6, 3e-5, 1e-4, 6e-4, 1e-3)] + [dielectric] )
			extra_section='%%cosmo  SMD true  epsilon %f  end' % dielectric # originals converged too soon, showing no concern for gradient convergence criteria! Replace with LooseOpt.
			atoms=files.read_xyz('SMRFF/lammps/%s_%s_%d.cluster.xyz' % (solute,solvent,i))
			old_name = '%s_%s.2_%d' % (solute,solvent,i)
			new_name = '%s_%s.21_%d' % (solute,solvent,i)
			if solute=='None':
				orca.job(new_name, '! OPT B97-D3 SV GCP(DFT/SV) ECP{def2-TZVP} COSMO Grid3 FinalGrid5 SlowConv LooseOpt', atoms, queue='batch', extra_section=extra_section, charge_and_multiplicity='0 1', previous=old_name)
			else:
				orca.job(new_name, '! OPT B97-D3 SV GCP(DFT/SV) ECP{def2-TZVP} COSMO Grid3 FinalGrid5 SlowConv LooseOpt', atoms, queue='batch', extra_section=extra_section, charge_and_multiplicity='2 1',previous=old_name)
			#orca.job('pb2+_%s_BP%d_test1' % (solvent,i), '! OPT BP D3BJ SV GCP(DFT/SV) ECP{def2-TZVP} COSMO Grid3 FinalGrid5 SlowConv LooseOpt', atoms, queue='batch', procs=4, extra_section=extra_section)

			#for a in atoms:
				#if a.element=='Pb':
					#a.element = 'Sn'
			#orca.job('pb2+_%s_H%d_test1' % (solvent,i), '! OPT HF-3c COSMO Grid3 FinalGrid5 SlowConv LooseOpt', atoms,  queue='batch', procs=4, extra_section=extra_section)
			
			#exit() #only do one of each