from merlin import *
import math, copy

names=['pb2+_nmp.6_20', 'pb2+_gbl.5_38','pb2+_acetone.4_46','pb2+_dmso.4_41','pb2+_DMF.4_45','pb2+_methacrolein.4_33','pb2+_ACN.4_49']
for name in names:
	atoms=orca.read(name).atoms
	bonds=utils.get_bonds(atoms)
	
	if 0:
		for b in bonds:
			if 'Pb' in [b.atoms[0].element, b.atoms[1].element]:
				print b.atoms[0].element, b.atoms[1].element, utils.dist(*b.atoms)
	if 0:
		angles, dihedrals = utils.get_angles_and_dihedrals(atoms)
		for a in angles:
			elements=[atom.element for atom in a.atoms]
			if elements==['O', 'Pb', 'O']:
				r = utils.dist(a.atoms[0], a.atoms[2])
				if r < 4.0:
					print a.theta, r

	def get_angle(a, center, b):
		A = math.sqrt((center.z-b.z)**2+(center.x-b.x)**2+(center.y-b.y)**2)
		N = math.sqrt((a.z-b.z)**2+(a.x-b.x)**2+(a.y-b.y)**2)
		B = math.sqrt((center.z-a.z)**2+(center.x-a.x)**2+(center.y-a.y)**2)
		theta = 180/math.pi*math.acos((A**2+B**2-N**2)/(2*A*B))
		return theta

	
	leads = [a for a in atoms if a.element=='Pb']
	angles = []
	Pb=leads[0]
	oxygens = [a for a in atoms if a.element in ['O','N'] and utils.dist(a,Pb)<3.1] 
	oxygens_labeled = copy.deepcopy(oxygens)

	bonds = []

	if 1:
		for center in oxygens_labeled:
			oxygens.sort(key=lambda x: utils.dist_squared(x,center))
			a, b = oxygens[1], oxygens[2]
			r_a = utils.dist(a,center)
			r_b = utils.dist(b,center)
			theta = get_angle(a, center, b)
			angles.append(theta)
			center.label = str('%.1f' % theta)

	files.write_cml(oxygens_labeled, bonds=bonds)

	#oxygens.sort(key=lambda x: utils.dist_squared(x,Pb))

	#print name, ','.join(['%.3f' % utils.dist(a,Pb) for a in oxygens]) # Pb-O distances don't show much correlation with solvent effectiveness: all solvents have fairly regular distances, max-min < 0.2 A
	#print name, len(angles), ','.join(['%.0f' % x for x in sorted(angles)])