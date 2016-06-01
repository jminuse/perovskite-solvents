'''makes various plots from solvent/solubility simulations'''



import math
import numpy as np
import matplotlib.pyplot as plt
import pylab


#solvents=[DMSO,DMF,NMP,Acetone,GBL,Methacrolein,ACN]
mayer_bond=[1.50, 1.88, 1.90, 1.99, 1.97, 1.97, 3.03]
solvents = ['DMSO', 'DMF', 'NMP', 'GBL', 'ACE', 'METH', 'ACN']
#H_solv_pure=[-0.6353340098,-0.626368262,-0.6252946962,-0.6083409691,-0.5980855101,-0.5943675572,-0.5826172304] #previously called BE_us. Order of solvents may be different. 
H_solv_DH = [-0.65695, -0.64212, -0.63867, -0.61263, -0.61222, -0.60409, -0.59594]
#pred_sol=[712.4040607378,175.9128305817,148.7864914525,10.566946856,2.133746383,1.1946803325,0.191059128]
#BE_us_exp=[-0.6353340098,-0.626368262,-0.6083409691,-0.5980855101]# dmso, dmf, acetone, gbl
exp_solvents = ['DMSO', 'DMF', 'GBL', 'ACE']
exp_H_solv_DH = [-0.65695, -0.64212, -0.61263, -0.61222]
exp_mayer_bond=[1.5006,1.8797,1.9679,1.9946]
exp_sol_I=[600,450,5,4]
exp_sol_Br=[560,350,4,4]
exp_sol_Cl=[310,17,2,2]

def one_at_a_time(xx,yy,xname,yname):
	plt.plot(xx,yy,marker='o',markersize=15,fillstyle='none',linestyle='--')
	plt.xlim([1,2.5])
	plt.ylim([-10,600])
	plt.xlabel(xname)
	plt.ylabel(yname)
	plt.title('%s vs %s' % (xname,yname))
	plt.legend(loc='lower right')
	plt.show()

def a_bunch():
	for x_axis,x_name in zip([mayer_bond, BE_us, BE_us_exp],['Mayer BO','BE_us','BE_us_exp']):
		for y_axis,y_name in zip([BE_us, exp_sol_I], ['BE_us', 'exp_sol_I']):
			if x_axis is y_axis: continue
			if len(x_axis)!=len(y_axis): continue
			one_at_a_time(x_axis,y_axis,x_name,y_name)

def predict_sol():
	plt.plot(mayer_bond,yy)

	plt.xlabel(xname)
	plt.ylabel(yname)
	plt.legend(loc='lower right')
	plt.show()

def experimental_solubility_vs_H_solv():
	from scipy.optimize import curve_fit

	#def exp_func(x, a, b):
	#	return a * np.exp(-b * x)
	#popt, pcov = curve_fit(exp_func, BE_us_exp, exp_sol_Cl, maxfev = 10000)
	#pred_sol = exp_func(np.array(BE_us_exp), *popt)

	#for x_axis,x_name in zip([BE_us_exp,exp_sol_Cl],['BE_us_exp',]):
	#	for y_axis, y_name, marker in zip([exp_sol_Cl,exp_sol_Br,exp_sol_I], ['PbCl$_2$','PbBr$_2$','PbI$_2$'],['o', 'd', 's']):
			#plt.plot([x*627.5 for x in x_axis],y_axis, marker= marker,markersize=15,fillstyle='none',linestyle='--', label=y_name)
	#		plt.errorbar(xx, yy, xerr=0.01, yerr=np.array(yy)*0.05+1, label=label, color=color)
	
	xx = np.array(exp_H_solv_DH)*627.5 #convert Hartree to kcal/mol
	for label, yy, color in zip(['PbCl$_2$','PbBr$_2$','PbI$_2$'], [exp_sol_Cl, exp_sol_Br, exp_sol_I], ['red', 'green', 'blue']):
		#plt.plot(xx,yy,marker=marker,markersize=15,fillstyle='none',linestyle='--',label=label)
		plt.errorbar(xx, yy, xerr=[1 for x in xx], yerr=np.array(yy)*0.05+1, label=label, color=color)
		for x,y,name in zip(xx,yy,exp_solvents):
			if name in ['GBL','ACE'] and label!='PbCl$_2$': continue
			x += (0.005 + (0.02 if name=='ACE' else 0) + (-0.03 if name=='GBL' else 0) + (-0.023 if name in ['GBL','ACE', 'DMF'] else 0))*40
			y += (-30 if name in ['GBL','ACE'] else 2 + (20 if name=='DMF' else 0))
			plt.annotate(name, xy=(x,y), textcoords='data', color='black')



	#axes.set_xlim([xmin,xmax])
	plt.ylim([-50,650])
	plt.xlabel('$\Delta H_{sol:Pb^{2+}}$ (kcal/mol)')
	plt.ylabel('Experimental Solubility of PbX$_2$ (mg/ml)')
	#plt.title('Experimental Solubility vs. Binding Energy')
	plt.legend(loc='upper right')
	#plt.yscale('log')
	plt.show()

#a_bunch()
#fitted()
#one_at_a_time(mb_exp, exp_sol_Br, ' Mayer Bond Order', 'Experimental Solubility PbBr2 (mg/ml)')

def experimental_solubility_vs_bond_order():
	xx = exp_mayer_bond
	for label, yy, color in zip(['PbCl$_2$','PbBr$_2$','PbI$_2$'], [exp_sol_Cl, exp_sol_Br, exp_sol_I], ['red', 'green', 'blue']):
		#plt.plot(xx,yy,marker=marker,markersize=15,fillstyle='none',linestyle='--',label=label)
		plt.errorbar(xx, yy, xerr=0.01, yerr=np.array(yy)*0.05+1, label=label, color=color)
		for x,y,name in zip(xx,yy,exp_solvents):
			if name in ['GBL','ACE'] and label!='PbCl$_2$': continue
			x += 0.005 + (0.01 if name=='ACE' else 0) + (-0.023 if name in ['GBL','ACE', 'DMF'] else 0)
			y += -30 if name in ['GBL','ACE'] else 2 + (20 if name=='DMF' else 0)
			plt.annotate(name, xy=(x,y), textcoords='data', color='black')
	xname, yname = 'Mayer Bond Order of Oxygen in Solvent', 'Experimental Solubility of PbX$_2$ (mg/ml)'
	plt.xlim([1.45, 2.05])
	plt.ylim([-50,650])
	plt.xlabel(xname)
	plt.ylabel(yname)
	#plt.title('%s vs %s' % (xname,yname))
	plt.legend(loc='upper right')
	plt.show()

#experimental_solubility_vs_H_solv()

#experimental_solubility_vs_bond_order()

def raiford_figure():
	names = ['ACE', 'GBL', 'DMF', 'DMSO', 'METH', 'ACN', 'NMP']
	data = [
	['Pb$^{2+}$', -0.0788914445, -0.076215144, -0.1053296833, -0.1180085172, -0.0659904223, -0.0732817183, -0.1027701253],
	['PbI$^{+}$', -0.0524488765, -0.0530955525, -0.0684701762, -0.0851442037, -0.0423638565, -0.0430857974, -0.0669988694],
	['PbBr$^{+}$', -0.0511217145, -0.0501855631, -0.0668157405, -0.0786317956, -0.0416426381, -0.0404635803, -0.0590874137],
	['PbCl$^{+}$', -0.0494389764, -0.049224192, -0.067754883, -0.0801128506, -0.040883084, -0.0400760729, -0.0613350137],
	['PbI$_{2}$', -0.0361529626, -0.0368506055, -0.0507690026, -0.0646378466, -0.0314229512, -0.0251905603, -0.0488884927],
	['PbBr$_{2}$', -0.0303604777, -0.0291544851, -0.0432005434, -0.0578393282, -0.0244069043, -0.0203233226, -0.0364956532],
	['PbCl$_{2}$', -0.0276761151, -0.0250951209, -0.036843793, -0.0515018571, -0.0155276667, -0.0209075154, -0.036961659],
	['PbI$_{2}$MA$^{+}$', -0.0380803683, -0.0293769547, -0.053923917, -0.0691437425, -0.0333819605, -0.0273126281, -0.0484740079],
	['PbBr$_{2}$MA$^{+}$', -0.0354505306, -0.0280302162, -0.0503579304, -0.0625508641, -0.0274422751, -0.0265962623, -0.0423983438],
	['PbCl$_{2}$MA$^{+}$', -0.0324334022, -0.0270145, -0.0443684691, -0.0601806086, -0.0248018225, -0.0224034316, -0.039732746],
	['PbI$_{3}$$^{-}$', -0.0198643798, -0.0202501431, -0.022107836, -0.0407779368, -0.0147906677, -0.012288481, -0.0237503258],
	['PbBr$_{3}$$^{-}$', -0.0138108573, -0.0157244099, -0.0211219314, -0.0271885547, -0.0084196779, -0.0067058051, -0.0148910401],
	['PbCl$_{3}$$^{-}$', -0.0099460424, -0.0135474684, -0.0192932974, -0.0180953348, -0.0020713644, -0.0044002078, -0.0158013889],
	['PbI$_{3}$MA', -0.024482342, -0.0237464578, -0.031201419, -0.0402857511, -0.0195162918, -0.0149161822, -0.0280573478],
	['PbBr$_{3}$MA', -0.019165515, -0.0134497968, -0.0259669675, -0.0372920672, -0.0135096993, -0.0083013844, -0.0209650393],
	['PbCl$_{3}$MA', -0.0154837231, -0.0145010498, -0.0222272135, -0.0341015516, -0.0106088562, -0.003455759, -0.0150285642],
	['I$^{-}$', -0.0072249622, -0.0109114748, -0.0090316264, -0.0018062828, -1.47987259425E-005, -0.0017910894, -0.0067247317],
	['Br$^{-}$', -0.0038800827, -0.003804442, -0.003251713, -0.0021027403, -0.0082909504, -0.0006038111, -0.0018363888],
	['Cl$^{-}$', -0.001028099, 0.0005361595, 0.0013630796, -0.0046132706, -0.0058360623, 0.0039727523, -0.0012783641]
	]

	H_solv = {}
	for i,n in enumerate(names):
		H_solv[n] = []
		for y in data:
			H_solv[n].append(y[i+1])

	solutes = []
	for y in data:
		solutes.append(y[0])

	H_solv = H_solv.items()
	H_solv.sort(key=lambda x:x[1][0])

	fig, ax = plt.subplots()
	ax.set_xticks([])

	for name,H in H_solv:
		H = np.array(H)*627.5
		#ax.plot(H, '-o', label=name)
		ax.errorbar(range(len(H)), H, xerr=0, yerr=1, label=name)

	for i,name in enumerate(solutes):
		ax.annotate(name, xy=(0 if i==0 else i*0.98-0.1*len(name)/6, 627.5*H_solv[ min(range(len(H_solv)),key=lambda j:H_solv[j][1][i]) ][1][i]-5), textcoords='data', color='black')

	plt.ylabel('$\Delta H_{sol:Pb^{2+}}$ (kcal/mol)')
	ax.legend(loc='lower right')
	plt.show()

def varun_figure():
	names = ['DMSO:DMF', 'DMSO:ACE', 'DMF:ACE']
	data = [
	[0,  -133.132552,  -93.693884,  -93.693884],
	[16.66,  -135.029284,  -102.779989,  -103.606707],
	[33.33,  -136.238506,  -120.745544,  -108.74951],
	[50,  -144.008948,  -130.823859,  -115.851043],
	[67,  -150.39208,  -139.059734,  -120.710116],
	[83.33,  -148.445792,  -150.071619,  -125.561869],
	[100,  -159.156304,  -159.156304,  -133.132552],
	]

	H_solv = {}
	for i,n in enumerate(names):
		H_solv[n] = []
		for y in data:
			H_solv[n].append(y[i+1])

	ratios = [y[0] for y in data]

	H_solv = H_solv.items()
	H_solv.sort(key=lambda x:x[1][0])

	for name,H in H_solv:
		H = np.array(H)*0.6
		#ax.plot(H, '-o', label=name)
		plt.errorbar(ratios, H, xerr=0, yerr=1, label=name)


	plt.xlabel('Composition (mol % of first solvent)')
	plt.ylabel('$\Delta H_{sol:Pb^{2+}}$ (kcal/mol)')

	plt.legend(loc='upper right')
	plt.show()

raiford_figure()
