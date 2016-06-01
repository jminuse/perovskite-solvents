import os
def run_on_queue(run_name, procs, queue, command):
	NBS = '''#!/bin/zsh
##NBS-name: "%s"
##NBS-nproc: %d
##NBS-queue: "%s"

source /fs/home/bas348/.zshrc

%s
''' % (run_name, procs, queue, command)
	f = open(run_name+'.nbs', 'w')
	f.write(NBS)
	f.close()
	os.system('jsub %s.nbs' % run_name)
	#os.system(command) #for debugging
	#exit()

def run():
	for i in range(0,20):
		for solvent in ['benzene','odcb','nitromethane']: #'methacrolein', 'gbl','ACN', 'DMF','dmso','nmp', 'acetone'
			for solute in ['pb2+']:
	#for (solute,solvent,i) in [('pb2+','acetone',10) ]:
				name = '%s_%s_%d' % (solute, solvent, i)

				if os.path.exists('lammps/%s.cluster.xyz' % name): continue

				command = '/fs/home/bas348/anaconda/bin/python smrff_example.py %s %s %s %d' % (name, solvent, solute, i+1)
				for suffix in ['.in', '_1.in', '.log', '_1.log', '.xyz', '_1.xyz']:
					if os.path.isfile('lammps/'+name+suffix):
						os.remove('lammps/'+name+suffix)
				for suffix in ['packed.xyz', '.packmol', 'packed.xyz_FORCED']:
					if os.path.isfile('packmol/'+name+suffix):
						os.remove('packmol/'+name+suffix)
				run_on_queue(name, 1, 'batch', command)
run()
