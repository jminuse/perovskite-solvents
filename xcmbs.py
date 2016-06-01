from merlin import *

frames=files.read_xyz('.xyz')

route = 'SP SCRF(Solvent=Acetone) guess=read SCF=QC'

g09.job('dblI_Cmbs', 'HSEH1PBE/GenECP '+route, atoms=frames, queue='batch', extra_section=
'''H C O Cl 0\ncc-pVDZ\n****
Pb 0\nSDD\n****


Pb 0\nSDD\n\n''')