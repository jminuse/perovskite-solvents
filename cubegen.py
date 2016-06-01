from merlin import *
from subprocess import Popen


# create an fchk file: this reads a check file from an old job and then writes formatted file
#cubegen(nprocs=0, kind: denisty=SCF, file_name.fchk, file_name.cube, npts=0, format=h, cubefile2(optional))
#for old_job in ['buty_solv','pbi2_buty_solv','pbi2_1buty_1.2','pbi2_1buty_2.2','2buty1.1_2','2buty1.2_2','2buty2.2_2','3buty1.1.1_4','3buty2.2.2_3','3buty1.1.2_3','3buty1.2.2_4','4from5.2221_3','4from5.1112_3','4buty2211_4','4buty1111_3','4from5.2222.2_3','5buty22111.2_2','pbcl2_buty_solv','pbcl2_1buty_1.2','pbcl2_1buty_2.2','2buty1.1_2_PbCl2','2buty1.2_2_PbCl2','2buty2.2_2_PbCl2','3buty2.2.2_3_PbCl2','3buty1.1.2_3_PbCl2','3buty1.2.2_4_PbCl2','3buty1.1.1_4_PbCl2_2','4from5.2221_3_PbCl2','4from5.1112_3_PbCl2','4buty2211_4_PbCl2','4buty1111_3_PbCl2','4from5.2222.2_3_PbCl2','5buty22111.2_2_PbCl2']:
for old_job in ['pbi2opt_1_HLYGAt','acetone_1_HLYGAt','pbi2_1acetone_2_HLYGA']:
	# Potential
	Popen('/usr/local/gaussian/g09/g09/formchk gaussian/%s.chk gaussian/%s.fchk' % (old_job,old_job), shell=True).wait()
	Popen('/usr/local/gaussian/g09/g09/cubegen 0 Potential=SCF gaussian/%s.fchk gaussian/%s.cube 0 h'% (old_job,old_job), shell=True).wait()
	# Density
	Popen('/usr/local/gaussian/g09/g09/formchk gaussian/%s.chk gaussian/%s.fchk' % (old_job,old_job+'_D'), shell=True).wait()
	Popen('/usr/local/gaussian/g09/g09/cubegen 0 Density=SCF gaussian/%s.fchk gaussian/%s.cube 0 h'% (old_job+'_D',old_job+'_D'), shell=True).wait()
	print("Generated %s" % (old_job+'_D'))

