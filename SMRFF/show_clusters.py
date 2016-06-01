# opens finished packmol simulations in VMD. Each frame is an iteration



from merlin import *

count = sys.argv[1]
for solvent in ['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']:
	f = open('pack_%s.xyz' %solvent , 'w')
	print solvent,
	for i in range(int(count)):
		f.write( open('lammps/pb2+_%s_%s.cluster.xyz' % (solvent,i)).read() ) # open file, read file, write file
		atoms = files.read_xyz( 'lammps/pb2+_%s_%s.cluster.xyz' % (solvent,i) )
		Pb= [a for a in atoms if a.element=='Pb'][0]
		Ox = [a for a in atoms if a.element=='N' and utils.dist(Pb, a) < 3]
		print len(Ox),
	print ''

'''for solute in ['pb2+']:
	for solvent in ['acetone','ACN','DMF','dmso', 'gbl', 'methacrolein', 'nmp']:
		energies = []
		for i in range(20):
			if os.path.isfile('lammps/%s_%s_%d_1.log' % (solute,solvent,i)):
				contents = open('lammps/%s_%s_%d_1.log' % (solute,solvent,i)).read()
				end = contents.rfind('Loop time of')
				start = contents.rfind('\n', 0, end)
				start = contents.rfind('\n', 0, start)
				e = float(contents[start:end].strip().split()[1])
				energies.append(e)
		energies.sort()
		print solute, solvent, ' '.join(['%.1f' % (e-min(energies)) for e in energies])'''