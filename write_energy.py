from merlin import *
import matplotlib.pyplot as plt
import cPickle as pickle

def BE():
	data = {}
	Pb_energy=orca.read('pb2+_vac.3').energy

	for solvent in ['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']:
		solvent_energies = []
		all_energies = []
		for i in range(50):
			pb_name = '%s_%s.3_%d' % ('pb2+',solvent,i)
			solvent_name = '%s_%s.3_%d' % ('None',solvent,i)
			if os.path.exists('orca/%s/%s.out'%(solvent_name, solvent_name)):
				solvent_energies.append( orca.read(solvent_name).energy )
			if os.path.exists('orca/%s/%s.out'%(pb_name, pb_name)):
				all_energies.append( orca.read(pb_name).energy )
		print solvent, sorted(all_energies)[1] - sorted(solvent_energies)[1] - Pb_energy

		data[solvent] = (solvent_energies, all_energies)

		plt.plot(sorted([x-min(all_energies) for x in all_energies]), label=solvent)

	plt.ylabel('E (Har)')
	plt.show()

	pickle.dump( data, open( "energies.3.pickle", "wb" ) )

def load_BE():
	data = pickle.load( open( "energies.3.pickle", "rb" ) )
	Pb_energy=orca.read('pb2+_vac.3').energy
	for solvent in ['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']:
		solvent_energies, all_energies = data[solvent]
		solvent_energies.sort()
		all_energies.sort()
		plt.plot([e - all_energies[0] for e in all_energies[:10]], label=solvent)

		print solvent, all_energies[1] - solvent_energies[1] - Pb_energy

	plt.ylabel('E (Har)')
	plt.show()

load_BE()