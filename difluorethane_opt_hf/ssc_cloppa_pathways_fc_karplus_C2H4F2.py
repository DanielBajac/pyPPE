import os
import sys
module_path = os.path.abspath(os.path.join('..'))

if module_path not in sys.path:
	sys.path.append(module_path)

from src.polaritization_propagator import Prop_pol as pp
from src.help_functions import extra_functions
from src.cloppa import Cloppa
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyscf import scf


F3_1s = [3, 3, 2, 2, 2, 3, 3, 2, 2, 3, 3, 3, 2, 2, 2, 3, 3, 2, 3]
F7_1s = [2, 2, 3, 3, 3, 2, 2, 3, 3, 2, 2, 2, 3, 3, 3, 2, 2, 3, 2]

F3_2s = [11, 10, 10, 11, 10, 10, 11, 10, 11, 10, 11, 10, 11, 10, 10, 11, 10, 11, 11]
F7_2s = [10, 11, 11, 10, 11, 11, 10, 11, 10, 11, 10, 11, 10, 11, 11, 10, 11, 10, 10]


F3_2pz = [8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
F7_2pz = [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]


F3_2p1 =[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
F7_2p1 =[5, 5, 6, 6, 6, 6, 6, 6, 5, 5, 5, 6, 6, 6, 6, 6, 6, 5, 5]

F3_2p2 = [7, 6, 5, 5, 5, 5, 5, 5, 6, 7, 6, 5, 5, 5, 5, 5, 5, 6, 7]
F7_2p2 = [6, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 6]

C1_1s = [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
C2_1s = [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]

C_C = [14, 14, 15, 15, 15, 15, 15, 15, 14, 14, 14, 15, 15, 15, 15, 15, 15, 14, 14]

occ_lmo = [(F3_1s,'F3_1s'), (F7_1s,'F7_1s'), (F3_2s,'F3_2s'), (F7_2s,'F7_2s'), (F3_2pz,'F3_2pz'), 
(F7_2pz,'F7_2pz'), (F3_2p1,'F3_2p1'), (F7_2p1,'F7_2p1'), (F3_2p2,'F3_2p2'), (F7_2p2,'F7_2p2'), 
(C1_1s,'C1_1s'), (C2_1s,'C2_1s'), (C_C,'C_C')]

v1_1= [73, 74, 74, 73, 73, 73, 73, 73, 74, 74, 73, 73, 73, 73, 73, 73, 73, 74, 74]
	   #0   1,  2,  3,  4,  5,  6,  7, 8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18 
v1_2= [74, 56, 73, 74, 75, 61, 75, 75, 73, 73, 74, 75, 75, 75, 74, 74, 75, 73, 73]

v2_1= [21, 21, 21, 20, 21, 21, 21, 21, 21, 22, 21, 21, 21, 21, 21, 21, 21, 21, 21]
v2_2= [22, 22, 22, 21, 25, 23, 22, 22, 22, 21, 22, 22, 23, 23, 25, 22, 22, 22, 22]


v3_1= [41, 40, 39, 40, 40, 40, 39, 40, 40, 41, 40, 40, 39, 40, 40, 40, 40, 40, 40]
v3_2= [40, 41, 40, 41, 44, 45, 43, 41, 39, 40, 41, 41, 43, 41, 41, 41, 41, 41, 41]


v4_1= [64, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 64]
	   #0   1,  2,  3,  4,  5,  6,  7, 8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18
v4_2= [63, 64, 64, 65, 62, 69, 69, 69, 69, 69, 65, 69, 69, 62, 67, 65, 64, 64, 63]

v6_1= [50, 50, 51, 51, 50, 51, 51, 50, 49, 50, 48, 49, 49, 51, 50, 50, 50, 49, 50]
v6_2= [49, 48, 48, 49, 48, 50, 50, 49, 50, 49, 51, 50, 51, 49, 51, 51, 49, 50, 49]


v5_1= [43, 45, 45, 43, 43, 46, 45, 45, 45, 45, 46, 45, 45, 45, 44, 44, 44, 45, 45]
	   #0   1,  2,  3,  4,  5,  6,  7, 8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18 
v5_2= [45, 51, 50, 50, 41, 41, 47, 48, 51, 46, 45, 48, 47, 46, 46, 49, 48, 51, 44]


v7_1= [68, 67, 67, 67, 68, 66, 67, 68, 67, 68, 68, 68, 67, 68, 66, 67, 68, 67, 68]
v7_2= [67, 69, 69, 69, 65, 68, 68, 67, 66, 65, 66, 67, 68, 66, 69, 69, 70, 69, 67]

v8_1= [69, 71, 71, 71, 70, 71, 71, 71, 71, 70, 70, 71, 71, 70, 71, 71, 71, 71, 70]
v8_2= [70, 70, 70, 70, 66, 67, 65, 64, 64, 64, 64, 64, 65, 65, 70, 70, 69, 70, 69]

v9_1= [62, 62, 62, 62, 61, 62, 62, 62, 62, 62, 61, 62, 62, 61, 62, 62, 62, 62, 61]
v9_2= [61, 68, 65, 64, 64, 64, 64, 65, 68, 61, 62, 65, 64, 64, 64, 64, 65, 68, 62]

v10_1= [66, 65, 66, 66, 67, 65, 66, 66, 65, 66, 67, 66, 66, 67, 65, 66, 66, 65, 66]
v10_2= [65, 66, 68, 68, 69, 70, 70, 70, 70, 67, 69, 70, 70, 69, 68, 68, 67, 66, 65]



lmo_vir = [(v1_1,"F3_2pz"),(v1_2,"F7_2pz"),(v2_1,"F3_3pz"),(v2_2,"F7_3pz"), (v3_1,"F3_3s"),(v3_2,"F7_3s"),
		  (v4_1,"F3_3dz"),(v4_2,"F7_3dz"), (v5_1,"F3_3py"), (v5_2,"F7_3py"),(v6_1,"F3_3px"),(v6_2,"F7_3px"),
		  (v7_1,"F3_3dxy"),(v7_2,"F7_3dxy"), (v8_1,"F3_3dx2-y2"),(v8_2,"F7_3dx2-y2"), 
		  (v9_1,"F3_3dyz"),(v9_2,"F7_3dyz"), (v10_1,"F3_3dxz"), (v10_2, "F7_3dxz") ]


for ang in range(10,11,1):
	ssc_tot = 0
	mol_loc, mo_coeff_loc, mo_occ_loc = extra_functions(
		molden_file=f"difluorethane_cc-pvdz_{ang*10}_Cholesky_PM.molden").extraer_coeff    
	cloppa_obj = Cloppa(
				mo_coeff_loc=mo_coeff_loc, mol_loc=mol_loc, #vir=viridx, occ=occidx,
				mo_occ_loc=mo_occ_loc)
	
	m = cloppa_obj.M(triplet=True)
	p = np.linalg.inv(m)        
	for i, ii in lmo_vir:
		for j, jj in lmo_vir:
			ssc = cloppa_obj.kernel_pathway(FC=True, FCSD=False, PSO=False,
											princ_prop=p,
											n_atom1=[2], occ_atom1=F3_2pz[ang], vir_atom1=j[ang], 
											n_atom2=[6], occ_atom2=F7_2pz[ang], vir_atom2=i[ang])
			ssc_tot += ssc
			#with open('cloppa_fc_virt_C2H4F2_ccpvdz.txt', 'a') as f:
			#	f.write(f'{ang*10} {ssc[0]} {ii} {jj} \n')     
			print(ii,jj, ssc, ssc_tot)
	print(ssc_tot, '-----> La suma de las contribuciones para el ??ngulo', ang*10)
	fc = cloppa_obj.kernel_pathway(FC=True, FCSD=False, PSO=False,
											princ_prop=p,
											n_atom1=[2], occ_atom1=F3_2pz[ang], 
											n_atom2=[6], occ_atom2=F7_2pz[ang])
	print(fc, '---------> lo que deber??a dar la suma de las contribuciones para el ??ngulo',ang*10)