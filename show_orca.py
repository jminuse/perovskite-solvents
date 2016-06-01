# opens orca simulations in VMD. Each frame is an iteration.



from merlin import *
import sys
import matplotlib.pyplot as plt

start,end = 0,50

for solvent in ['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']:
	jobs = [ orca.read('pb2+_%s.3_%s' % (solvent,i)) for i in range(start,end) ]
	jobs.sort(key=lambda j: j.energy if j.energy is not None else 1e10)
	'''
	for j in jobs:
		pb = [a for a in j.atoms if a.element=='Pb'][0]
		count_o = 0
		for a in j.atoms:
			if a.element=='O':
				if utils.dist(a,pb) < 3.0:
					count_o += 1
		print j.energy-min([jj.energy for jj in jobs]), count_o
	'''
	import matplotlib.pyplot as plt

	energies = [j.energy for j in jobs if j.energy is not None]
	print solvent, min(energies), jobs[0].name, jobs[1].name
	energies = [(e-min(energies))/0.001 for e in energies ]

	#energies = [j.energies[-1]-j.energies[0] for j in jobs if j.energy is not None]
	#print solvent, max(energies)
	
	plt.plot(sorted(energies), label=solvent)
	
	frames = [j.atoms for j in jobs]

	utils.procrustes(frames)

	files.write_xyz( frames, solvent+'_orca' )

plt.legend()
plt.ylabel('Sample number')
plt.ylabel('E (kT)')
plt.show()