'''reads file and extracts SCf and MP2 energies..energies are all on one line.'''


from merlin import *



'''def get_SCF(name):
	if not os.path.isfile('orca/%s/%s.out' % (name,name)):
		return None
	for line in open('orca/%s/%s.out' % (name,name)):
		if line.startswith('Total Energy   '):
			SCF=float(line.split()[3])
			return SCF'''

def get_final(name):
	if not os.path.isfile('orca/%s/%s.out' % (name,name)):
		return None
	for line in open('orca/%s/%s.out' % (name,name)):
		if line.startswith('FINAL SINGLE POINT ENERGY'):
			SCF=float(line.split()[4])
			return SCF



nmp_SCFs=[]
#nmp_mp2s=[]
for i in range(20):
	scf_file = 'pb2+_nmp.6_%d' % (i)
	#mp2_file = 'pb2+_nmp.6_%d' % (i)

	SCF=get_SCF(scf_file)
	#MP2=get_SCF(mp2_file)

	if SCF:
		print i, SCF#, MP2






	






