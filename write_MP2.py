from merlin import *
import matplotlib.pyplot as plt
import cPickle as pickle
import math

output = open('MP2_energies.csv', 'w')
output.write('Filename, SP_Energy\n')

def is_converged(name):
	return os.path.exists('orca/%s/%s.out'%(name, name)) and '****ORCA TERMINATED NORMALLY****' in open('orca/%s/%s.out'%(name,name)).read()
	#return os.path.exists('orca/%s/%s.out'%(name, name)) and 'ABORTING THE RUN' not in open('orca/%s/%s.out'%(name,name)).read()

def read_data():
	all_energies = {}
	for solvent in ['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']:
		for solute in ['None', 'pb2+']:
			energies = []
			for i in range(50):
				old_name1 = '%s_%s.4_%d' % (solute,solvent,i)
				old_name2 = '%s_%s.5_%d' % (solute,solvent,i)

				for name in [old_name1, old_name2]:
					if is_converged(name):
						energy = orca.read(name).energy
						#output.write( '%s %f\n' % (name, energy))
						energies.append(energy)
			if energies:
				#energies.sort()
				#energies = [e-energies[0] for e in energies]
				#plt.plot(energies, label=solvent+'/'+solute)
				all_energies[ (solvent,solute) ] = energies

	pickle.dump( all_energies, open('pickled_double_hybrids.pickle', 'w') )

	#plt.legend()
	#plt.ylabel('E (Har)')
	#plt.show()

def plot_data():
	all_energies = pickle.load( open('pickled_double_hybrids.pickle') )
	for solvent in['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']:
		for solute in ['None', 'pb2+']:
			if (solvent,solute) in all_energies:
				energies = all_energies[ (solvent,solute) ]
				energies.sort()
				energies = [(e-energies[0])*1000 for e in energies]
				plt.plot(energies, label=solvent+'/'+solute)
	plt.legend()
	plt.ylabel('E (kT)')
	plt.show()

def exponential_average(v, kT=0.001):
	min_v = min(v)
	return sum([x*math.exp(-(x-min_v)/kT) for x in v]) / sum([math.exp(-(x-min_v)/kT) for x in v])

def get_binding_energies():
	#av = exponential_average
	av = min
	all_energies = pickle.load( open('pickled_double_hybrids.pickle') )
	#meatball = orca.read('pb2+_vac.4.1').energy #double-hybrid quadruple-zeta
	meatball = orca.read('pb2+_vac.3').energy #pure-DFT triple-zeta
	for solvent in['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']:
		if all( [ ((solvent,solute) in all_energies) for solute in ['None', 'pb2+'] ] ):
			spaghetti = av( all_energies[ (solvent,'None') ] )
			spaghetti_and_meatball = av( all_energies[ (solvent,'pb2+') ] )

			E = spaghetti_and_meatball - meatball - spaghetti

			print solvent, E




def get_pure_DFT_binding_energies():

	all_energies = {}
	for solvent in['benzene', 'odcb', 'nitromethane']:
	#for solvent in ['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']:
		for solute in ['None', 'pb2+']:
			energies = []
			for i in range(20):
				name = '%s_%s_tz.1_%d' % (solute,solvent,i)
				#name = '%s_%s.3_%d' % (solute,solvent,i)
				energy = orca.read(name).energy
				energies.append(energy)
			if energies:
				all_energies[ (solvent,solute) ] = energies
				print solvent, solute, [e for e in sorted(energies) if e is not None][:3]

get_pure_DFT_binding_energies()