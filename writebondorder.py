# opens orca out file and reads mayer bond order data for each bond in the single solvent molecule



import re
element1s = {}
element2s = {}
orders = {}

names = []
for solvent in ['DMF','dmso','nmp','methacrolein','ACN','gbl','acetone']: #
	name='%s_.4'% (solvent)
	names.append(name)
	contents= open('orca/%s/%s.out' % (name,name)).read()
	element1s[name] = []
	element2s[name] = []
	orders[name] = []
	bonds = re.findall('B\( +(\d+)-(\w+) ?, +(\d+)-(\w+) ?\) : +(\S+)', contents)
	for bond in bonds: #len(bonds)/2 :
		element1 = bond[1]
		element2 = bond[3]
		order = bond[4]
		element1s[name].append(element1)
		element2s[name].append(element2)
		orders[name].append(order)

max_len=max([len(element1s[n]) for n in names])

csv = open('single_solvent_bond_order.csv', 'w')

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






































