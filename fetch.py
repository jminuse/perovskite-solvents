charges={}# dictionary
elements={}

for name in ['acetone_1_HLYGAt', 'pbi2opt_1_HLYGAt']:
	contents= open('gaussian/%s.log' % name).read()
	start=contents.rfind('Mulliken charges:')
	end=contents.find('Sum of Mulliken charges')
	lines=contents[start:end].splitlines()
	charges[name]=[]
	elements[name]=[]
	for line in lines:
		a=line.split()
		if len(a)==3:
			charges[name].append(a[2])
			elements[name].append(a[1])

max_len=max([len(charges[n])for n in charges])

csv = open('charges.csv', 'w')

for name in charges:
	csv.write('%s,,' % (name) )
csv.write('\n')
for name in charges:
	csv.write('element,charge,')
csv.write('\n')
for row in range(max_len):
	for name in charges:
		if row < len(charges[name]):
			csv.write('%s,%s,' % (elements[name][row],charges[name][row]))
		else:
			csv.write (',,')
	csv.write('\n')
