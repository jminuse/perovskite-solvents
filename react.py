import sys
sys.path.append('/fs/home/jms875/Library')
import gaussian, filetypes

def start_stuff():
	for step in range(10):
		gaussian.job( filetypes.parse_xyz('xyz/3_1_1_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'n_3_1_1_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 29 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_1_1_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'i_3_1_1_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_1_1_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'both_3_1_1_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nB 13 29 F\nA 13 36 29 F\nA 36 13 29F')
		gaussian.job( filetypes.parse_xyz('xyz/3_2_1_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'n_3_2_1_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 29 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_2_1_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'i_3_2_1_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_2_1_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'both_3_2_1_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nB 13 29 F\nA 13 36 29 F\nA 36 13 29F')
		gaussian.job( filetypes.parse_xyz('xyz/3_3_1_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'n_3_3_1_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 29 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_3_1_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'i_3_3_1_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_3_1_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'both_3_3_1_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nB 13 29 F\nA 13 36 29 F\nA 36 13 29F')
		gaussian.job( filetypes.parse_xyz('xyz/3_1_2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'n_3_1_2_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 29 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_1_2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'i_3_1_2_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_1_2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'both_3_1_2_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nB 13 29 F\nA 13 36 29 F\nA 36 13 29F')
		gaussian.job( filetypes.parse_xyz('xyz/3_2_2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'n_3_2_2_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 29 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_2_2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'i_3_2_2_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_2_2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'both_3_2_2_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nB 13 29 F\nA 13 36 29 F\nA 36 13 29F')
		gaussian.job( filetypes.parse_xyz('xyz/3_3_2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'n_3_3_2_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 29 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_3_2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'i_3_3_2_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nA 13 29 36 F\nA 29 13 36F')
		gaussian.job( filetypes.parse_xyz('xyz/3_3_2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'both_3_3_2_dmf_dma_pbi2_%d' % step, 'Opt=ModRedundant', extra_section='B 13 36 F\nB 13 29 F\nA 13 36 29 F\nA 36 13 29F')

def approach():
	for step in range(10):
		gaussian.job( [], 'HSEH1PBE/LanL2DZ', 'batch', 'pb_n2_%d' % step, 'Opt=ModRedundant Geom=(Checkpoint,NewDefinition)', extra_section='B 2 10 F', previous='pb_n_%d' % step)
		gaussian.job( [], 'HSEH1PBE/LanL2DZ', 'batch', 'pb_i2_%d' % step, 'Opt=ModRedundant Geom=(Checkpoint,NewDefinition)', extra_section='B 10 12 F', previous='pb_i_%d' % step)
		gaussian.job( [], 'HSEH1PBE/LanL2DZ', 'batch', 'pb_both2_%d' % step, 'Opt=ModRedundant Geom=(Checkpoint,NewDefinition)', extra_section='B 2 10 F\nB 10 12 F', previous='pb_both_%d' % step)

def dmf1():
	for step in range(5):
		gaussian.job( filetypes.parse_xyz('xyz/2_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', '2_dmf_dma_pbi2_%d' % step, 'opt')

def dmf2():
	for step in range(9):
		gaussian.job( filetypes.parse_xyz('xyz/3_dmf_dma_pbi2_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', '3_dmf_dma_pbi2_%d' % step, 'opt')

def opt():
	gaussian.job( filetypes.parse_xyz('xyz/2_dmf_dma_pbi2_1.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', '2_dmf_dma_pbi2_1', 'opt')


def nest():
	for i in range(3):
		for j in range(5):
			print 'My name is Spencer, %d and I have %d years of experience' % (i,j)

def opt1():
	gaussian.job( filetypes.parse_xyz('xyz/3_2_2_dmf_dma_pbi2_7.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'x_both_3_2_2_dmf_dma_pbi2_7', 'Opt', extra_section='B 13 36 F\nB 13 29 F\nA 13 36 29 F\nA 36 13 29F')
	gaussian.job( filetypes.parse_xyz('xyz/3_1_2_dmf_dma_pbi2_7.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'x_both_3_1_2_dmf_dma_pbi2_7', 'Opt', extra_section='B 13 36 F\nB 13 29 F\nA 13 36 29 F\nA 36 13 29F')
	gaussian.job( filetypes.parse_xyz('xyz/3_3_1_dmf_dma_pbi2_7.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'x_both_3_3_1_dmf_dma_pbi2_7', 'Opt', extra_section='B 13 36 F\nB 13 29 F\nA 13 36 29 F\nA 36 13 29F')
	gaussian.job( filetypes.parse_xyz('xyz/3_2_2_dmf_dma_pbi2_7.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'x_n_3_2_2_dmf_dma_pbi2_7', 'Opt', extra_section='B 13 29 F\nA 13 29 36 F\nA 29 13 36F')
	gaussian.job( filetypes.parse_xyz('xyz/3_1_2_dmf_dma_pbi2_7.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'x_n_3_1_2_dmf_dma_pbi2_7', 'Opt', extra_section='B 13 29 F\nA 13 29 36 F\nA 29 13 36F')
	gaussian.job( filetypes.parse_xyz('xyz/3_2_2_dmf_dma_pbi2_7.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'x_i_3_2_2_dmf_dma_pbi2_7', 'Opt', extra_section='B 13 36 F\nA 13 29 36 F\nA 29 13 36F')
	gaussian.job( filetypes.parse_xyz('xyz/3_1_2_dmf_dma_pbi2_7.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'x_i_3_1_2_dmf_dma_pbi2_7', 'Opt', extra_section='B 13 36 F\nA 13 29 36 F\nA 29 13 36F')
	gaussian.job( filetypes.parse_xyz('xyz/3_3_1_dmf_dma_pbi2_7.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'x_i_3_3_1_dmf_dma_pbi2_7', 'Opt', extra_section='B 13 36 F\nA 13 29 36 F\nA 29 13 36F')

def opt2():
	gaussian.job( filetypes.parse_xyz('xyz/DMSO.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'DMSO', 'Opt')

def dmso():
	for step in range(7):
		gaussian.job( filetypes.parse_xyz('xyz/4_dp_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', '4_dp_%d' % step, 'opt')

def d2o():
	for step in range(3,4):
		gaussian.job( filetypes.parse_xyz('xyz/pbi2_d2o_%d.xyz' % step), 'HSEH1PBE/LanL2DZ', 'batch', 'pbi2_d2o_%d' % step, 'opt guess=read geom=(read,newdefinition)', previous='')

def opt_acetone():
	#gaussian.job( filetypes.parse_xyz('xyz/acetone.xyz'), 'PM6', 'batch', 'acetone_pm6', 'Opt')
	gaussian.job([], 'HSEH1PBE/LanL2DZ', 'batch', 'acetone', 'Opt guess=read geom=(check,newdefinition)', previous='acetone_pm6')

def acetone_and_pbi2():
	acetone1 = gaussian.atoms('acetone')
	pbi2 = filetypes.parse_xyz('xyz/Optimized Molecules/pbi2.xyz')

	for atom in acetone1:
		atom.x = atom.x + 10
	

	atoms = acetone1+pbi2

	filetypes.write_xyz('pbi2_1acetone', atoms)
acetone_and_pbi2 ()

def acetone():
	gaussian.job( [], 'HSEH1PBE/LanL2DZ', 'batch', 'pbi2_1acetone_2', 'opt guess=read geom=(check,newdefinition)', previous='pbi2_1acetone_1')
	#gaussian.job( filetypes.parse_xyz('xyz/pbi2_1acetone_1.xyz'), 'PM6', 'batch', 'pbi2_1acetone_1', 'Opt')

def optpbi2():
	gaussian.job( [], 'HSEH1PBE/LanL2DZ', 'batch', 'pbi2opt_0', 'opt guess=read geom=(check,newdefinition)', previous='pbi2')
	#gaussian.job( filetypes.parse_xyz('xyz/pbi2.xyz'), 'HSEH1PBE/LanL2DZ', 'batch', 'pbi2', 'Opt')
optpbi2()








