[smd325@istabraq]~/Desktop/Blaire/Documents/perovskites/gaussian% /usr/local/gaussian/g09/g09/formchk acetone_1_HLYGAt.chk                     
 Read checkpoint file acetone_1_HLYGAt.chk
 Write formatted file acetone_1_HLYGAt.fchk
 Coordinates translated and rotated.
 Coordinates match /B/ after translation and rotation.
 Rotating derivatives, DoTrsp=T IDiff= 1 LEDeriv=   1493 LFDPrp=       0 LDFDPr=       0.
[smd325@istabraq]~/Desktop/Blaire/Documents/perovskites/gaussian% /usr/local/gaussian/g09/g09/cubegen 0 Density=SCF acetone_1_HLYGAt.fchk  acetone.cube      
[smd325@istabraq]~/Desktop/Blaire/Documents/perovskites/gaussian% ls acetone.cube
acetone.cube
[smd325@istabraq]~/Desktop/Blaire/Documents/perovskites/gaussian% vmd acetone.cube
Info) VMD for LINUXAMD64, version 1.9 (March 14, 2011)
Info) http://www.ks.uiuc.edu/Research/vmd/                         
Info) Email questions and bug reports to vmd@ks.uiuc.edu           
Info) Please include this reference in published work using VMD:   
Info)    Humphrey, W., Dalke, A. and Schulten, K., `VMD - Visual   
Info)    Molecular Dynamics', J. Molec. Graphics 1996, 14.1, 33-38.
Info) -------------------------------------------------------------
Info) Multithreading available, 2 CPUs detected.
Info) Free system memory: 647MB (34%)
Info) No CUDA accelerator devices available.
Warning) Detected X11 'Composite' extension: if incorrect display occurs
Warning) try disabling this optional X server feature.
Info) OpenGL renderer: Mesa DRI Intel(R) 965Q 
Info)   Features: STENCIL MDE CVA MTX NPOT PP PS GLSL(OVF) 
Info)   Full GLSL rendering mode is available.
Info)   Textures: 2-D (8192x8192), 3-D (256x256x256), Multitexture (8)
Info) Dynamically loaded 2 plugins in directory:
Info) /fs/home/jds429/library/vmd/plugins/LINUXAMD64/molfile
Info) File loading in progress, please wait.
Info) Using plugin cube for structure file acetone.cube
cubeplugin) trying to read cube data set 0
Info) Analyzing Volume...
Info)    Grid size: 93x80x68  (7 MB)
Info)    Total voxels: 505920
Info)    Min: 0.000000  Max: 2.175660  Range: 2.175660
Info)    Computing volume gradient map for smooth shading
Info) Added volume data, name=acetone.cube : Gaussian Cube:  run by gaussian.py Density=SCF
Info) Using plugin cube for coordinates from file acetone.cube
Info) Determining bond structure from distance search ...
Info) Finished with coordinate file acetone.cube.
Info) Analyzing structure ...
Info)    Atoms: 10
Info)    Bonds: 9
Info)    Angles: 0  Dihedrals: 0  Impropers: 0  Cross-terms: 0
Info)    Bondtypes: 0  Angletypes: 0  Dihedraltypes: 0  Impropertypes: 0
Info)    Residues: 1
Info)    Waters: 0
Info)    Segments: 1
Info)    Fragments: 1   Protein: 0   Nucleic: 0
vmd > ^C

