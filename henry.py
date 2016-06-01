from merlin import *
#g09.binding_energy_dz('4ACN_s_4', 'pbi2_3acetoN_42', 'aceto_2', range (21))

for job in ['4ACN_s_4','4ACN_s_4_A0_1','4ACN_s_4_B0_1','pbi2_3acetoN_42_AB0_1','aceto_2_AB0_2','pbi2_3acetoN_42','aceto_2']:
	 print job,gaussian.parse_atoms(job)[0]

