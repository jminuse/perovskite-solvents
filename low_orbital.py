# takes data  from James' simulations on lead halide and solvents, and writes a csv file extracting lowedin orbital and charge information for each element



orbitals={}# dictionary
elements={}
charges={}
#'pb++','pbbr+',


def find_by_header(contents, header, footer):
	start=contents.rfind(header)
	end=contents.find(footer, start)
	start=contents.find('\n', start)
	return contents[start:end]



for solute in ['pbbr2','pbbr3']: #'pb++','pbbr+',
	for solvent in ['dmf','dmso','nmp','methc','buty','nitr','acetone']:
		name='%s_%s_ma_aug3'% (solute, solvent)
		contents= open('/fs/home/jms875/Documents/perovskites/orca/%s/%s.out' %(name, name)).read()
		lines=find_by_header(contents, 'LOEWDIN REDUCED ORBITAL CHARGES', '*****************************').splitlines()
		charges[name]=[]
		elements[name]=[]
		orbitals[name]=[]
		current_element = ''
		for line in lines:
			if len(line)==46:
				if line[4:6].strip():
					current_element = line[4:6].strip()
				print current_element, line
				if current_element in ('Pb','O', 'N'):
					elements[name].append( current_element )
					orbitals[name].append(line[30].strip())
					charges[name].append(line[35:].strip())

max_len=max([len(elements[n])for n in elements])


csv = open('orca_orbital_br_ma.csv', 'w')

for name in elements:
	csv.write('%s,,,' % (name) )
csv.write('\n')
for name in elements:
	csv.write('element,orbital,charge,')
csv.write('\n')
for row in range(max_len):
	for name in elements:
		if row < len(elements[name]):
			csv.write('%s,%s,%s,' % (elements[name][row],orbitals[name][row],charges[name][row]))
		else:
			csv.write (',,,')
	csv.write('\n')