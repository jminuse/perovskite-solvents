import sys
sys.path.append('/fs/home/jms875/Library')
import filetypes

output = sys.argv[2] if len(sys.argv)>2 else 'out.xyz'
filetypes.gaussian_to_xyz('gaussian/'+sys.argv[1]+'.log', output)

