import math, copy, sys, random, re, os, cPickle, shutil
sys.path.append("/fs/home/jms875/Library") 
import gaussian, filetypes, utils

name = sys.argv[1]
if len(sys.argv)==3:
	low=0
	count = int(sys.argv[2])
if len(sys.argv)==4:
	low = int(sys.argv[2])
	count = int(sys.argv[3])

f = open('out.xyz', 'w')
energies = []
for step in range(low,count):
	energy, atoms = gaussian.parse_atoms(name%step, check_convergence=False)
	filetypes.write_xyz('', atoms, f)
	print energy, int(gaussian.parse_atoms(name%step)!=None)
	energies.append(energy)

def matplot(y):
	import matplotlib.pyplot as plt
	plt.plot(y,marker='.')
	plt.show()

f.close()
energies = [(e-energies[0])*627.5 for e in energies]
matplot(energies)

