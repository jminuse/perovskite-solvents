# opens and reads orca file and writes to a csv the Mulliken global atomic charge, and the mayer total valence


Mulliken_GAC={}# dictionary
elements={}
Mayer_total_valence={}



def find_by_header(contents, header, footer):
	start=contents.rfind(header)
	end=contents.find(footer, start)
	start=contents.find('\n', start)
	return contents[start:end]

names=['DMF','dmso','methacrolein','nmp', 'ACN','gbl','acetone']
print '%20s %20s %20s' % ('Name', 'O-charge', 'O-valence')
for name in names:
	contents= open('orca/%s/%s.out' %(name, name)).read()
	lines=find_by_header(contents, 'ATOM       NA         ZA         QA         VA         BVA        FA', '\n\n').splitlines()
	for line in lines:
		a=line.split()
		if len(a)>6:
			if a[1] == 'O':
				print '%20s %20s %20s' % (name, a[4], a[5])


names = []
for solvent in ['DMF','dmso','methacrolein','nmp', 'ACN','gbl','acetone']: 
		name='%s_.4'% (solvent)
		contents= open('orca/%s/%s.out' % (name,name)).read()	
		lines=find_by_header(contents, 'ATOM       NA         ZA         QA         VA         BVA        FA', '\n\n').splitlines()
		Mulliken_GAC[name]=[]
		elements[name]=[]
		Mayer_total_valence[name]=[]
		for line in lines:
			a=line.split()
			if len(a)>6:
				elements[name].append(a[1])
				Mulliken_GAC[name].append(a[4])
				Mayer_total_valence[name].append(a[5])

max_len=max([len(elements[n])for n in elements])


csv = open('single_solvent_valence.csv', 'w')

for name in elements:
	csv.write('%s,,,' % (name) )
csv.write('\n')
for name in elements:
	csv.write('element,Mulliken_GAC,Mayer_total_valence,')
csv.write('\n')
for row in range(max_len):
	for name in elements:
		if row < len(elements[name]):
			csv.write('%s,%s,%s,' % (elements[name][row],Mulliken_GAC[name][row],Mayer_total_valence[name][row]))
		else:
			csv.write (',,,')
	csv.write('\n')
