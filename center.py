from merlin import *

f= files.read_xyz('test.xyz')
utils.center_frames([f], [1,0,2])
files.write_xyz(f,'t0')
for i in range(1,20):
	f[0].x += 0.5
	files.write_xyz(f,'t%d'%i)

frames=[]
for i in range(20):
	frames.append(files.read_xyz('t%d.xyz' %i))

files.write_xyz(frames,'act.final')
