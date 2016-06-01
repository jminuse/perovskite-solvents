from merlin import *
job_names = ['4ACN_s_4', '4ACN_s_4_A0_1', '4ACN_s_4_B0_1', 'pbi2_3acetoN_42_AB0_1', 'aceto_2_AB0_2', 'pbi2_3acetoN_42', 'aceto_2']
# Check if jobs are still running
for s in log.get_jlist():
	if s in job_names:
		print("Sorry, all simulations haven't finished yet...")
		sys.exit()

# Else, we can get the energy
energies = []
for s in job_names:
	e,_ = g09.parse_atoms(s)
	energies.append(e)

sp_corr = energies[0] - energies[1] - energies[2]
geom_corr = energies[3] - energies[5] + energies[4] - energies[6]
print('Jobs Calculated From: '+'\n\t'.join(job_names))
print('------------')
print('Superposition Correction = '+str(sp_corr)+' Ha')
print('Geometry Correction = '+str(geom_corr)+' Ha')
print('Binding Energy = '+str(sp_corr + geom_corr)+' Ha')