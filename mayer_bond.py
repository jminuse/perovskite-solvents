# takes james' data on lead halide and solvent simulations and reads file for mayer bond order between Pb and atoms that are bonded to it. 


import re
element1s = {}
element2s = {}
orders = {}

#names = ['triMP_opt']
#for solute in [ 'pbi2', 'pbi3']: #'pb++','pbbr+',
#	for solvent in ['dmf','dmso','nmp','methc', 'nitr','buty','acetone']:
#		name='%s_%s_ma_aug3'% (solute, solvent)
#		names.append(name)
names=['acetone','DMF','dmso','gbl', 'methacrolein', 'nmp', 'ACN']

names = [name + '_TZ' for name in names]

for name in names:#/fs/home/jms875/Documents/perovskites/
	contents= open('orca/%s/%s.out' %(name, name)).read()
	
	element1s[name] = []
	element2s[name] = []
	orders[name] = []
	bonds = re.findall('B\( +(\d+)-(\w+) ?, +(\d+)-(\w+) ?\) : +(\S+)', contents)
	for bond in bonds: #len(bonds)/2 :
		element1 = bond[1]
		element2 = bond[3]
		order = bond[4]
		if 'N' in (element1,element2):
			element1s[name].append(element1)
			element2s[name].append(element2)
			orders[name].append(order)

max_len=max([len(element1s[n]) for n in names])

csv = open('mayer_bonds_TZ.csv', 'w')

for name in names:
	csv.write('%s,,,' % (name) )
csv.write('\n')
for name in names:
	csv.write('element1,element2,order,')
csv.write('\n')
for row in range(max_len):
	for name in names:
		if row < len(element1s[name]):
			csv.write('%s,%s,%s,' % (element1s[name][row],element2s[name][row],orders[name][row]))
		else:
			csv.write (',,,')
	csv.write('\n')