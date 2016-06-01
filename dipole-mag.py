import re

for solvent in ['DMF','dmso','nmp','methacrolein','ACN','gbl','acetone']: #
	name='%s_.4'% (solvent)
	contents= open('orca/%s/%s.out' % (name,name)).read()
	dipole = re.findall('Magnitude \(a.u.\) +: +(\S+)', contents)[0]
	print solvent, dipole
