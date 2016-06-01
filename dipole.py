from merlin import *


for solvent in ['DMF','dmso','nmp','methacrolein','ACN','gbl','acetone']: 
	name='%s_.4'% (solvent)
	job=orca.read(name)
	oxygens = [a for a in job.atoms if a.element=='N']
	print solvent
	for o in oxygens:
		bonded = sorted(job.atoms, key=lambda a:utils.dist(o,a))[1]
		dipole = o.charge*bonded.charge/utils.dist(o,bonded)
		print '\t', dipole