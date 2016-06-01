Echarges={}
Mcharges={} # dictionary
elements={}

names =['methc_solv_Imbs_HLYGAt','pbi2_solv_methc_Imbs_HLYGAt','pbi2_1methc_4_Imbs_HLYGAt','pbi2_2methc_6_Imbs_HLYGAt','pbi2_3methc_9_Imbs_HLYGAt','pbi2_4methc_9_Imbs_HLYGAt','pbi2_5methc_12_Imbs_HLYGAt','pbi2_6methc_9_Imbs_HLYGAt','methc_solv_Cmbs_HLYGAt','pbcl2opt_0_Cmbs_HLYGAt','pbcl2_1methc_4_Cmbs_HLYGAt','pbcl2_2methc_6_Cmbs_HLYGAt','pbcl2_3methc_9_Cmbs_HLYGAt','pbcl2_4methc_10_Cmbs_HLYGAt','pbcl2_5methc_12_Cmbs_HLYGAt','pbcl2_6methc_9_Cmbs_HLYGAt']
for name in names:
	contents= open('gaussian/%s.log' % name).read()
	start=contents.rfind('Mulliken charges:')
	end=contents.find('Sum of Mulliken charges')
	lines=contents[start:end].splitlines()
	Mcharges[name]=[]
	elements[name]=[]
	for line in lines:
		a=line.split()
		if len(a)==3:
			Mcharges[name].append(a[2])
			elements[name].append(a[1])


	contents= open('gaussian/%s.log' % name).read()
	start=contents.rfind('ESP charges:')
	end=contents.find('Sum of ESP charges')
	lines=contents[start:end].splitlines()
	Echarges[name]=[]
	for line in lines:
		a=line.split()
		if len(a)==3:
			Echarges[name].append(a[2])		

max_len=max([len(Echarges[n])for n in Echarges])

csv = open('Methc_mbs_charges.csv','w')

for name in names:
	csv.write('%s,,,,' % (name) )
csv.write('\n')
for name in names:
	csv.write('element,Echarge,Mcharge,,')
csv.write('\n')
for row in range(max_len):
	for name in names:
		if row < len(Echarges[name]):
			csv.write('%s,%s,%s,,' % (elements[name][row],Echarges[name][row],Mcharges[name][row]))
		else:
			csv.write (',,,,')
	csv.write('\n')
