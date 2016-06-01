from merlin import *

#utils.opt_opls('methacrolein', taboo_time=10)

extra = { (19, 66): (47, 3, 46):(85.00, 120.00), (47, 47, 3, 46):(0.0, 14.0, 0.0, 0.0) }

#torsion      46   47   47   46      0.000 0.0 1  14.000 180.0 2   0.000 0.0 3

for name in ['pbcl_p']:
	print utils.Molecule('cml/'+name, check_charges= False)

#2 6 [20, 48, 48, 13, 48, 49, 46, 46, 46, 49, 49]
#2 4 [5, 48, 48, 13, 48, 49, 46, 46, 46, 49, 49]
#2 17 [20, 48, 48, 13, 48, 49, 46, 46, 46, 49, 49]