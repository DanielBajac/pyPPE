import os
import sys
module_path = os.path.abspath(os.path.join('..'))

if module_path not in sys.path:
    sys.path.append(module_path)

from src.ppe import inverse_principal_propagator 

#from src.ppe import inverse_principal_propagator
from src.help_functions import extra_functions
import itertools
import plotly.express as px
import pandas as pd


o1= [8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
       #0   1,  2,  3,  4,  5,  6,  7, 8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18 

o2= [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]


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


#falta agregar los orbitales 3dy. 
v5_1= [43, 45, 45, 43, 43, 46, 45, 45, 45, 45, 46, 45, 45, 45, 44, 44, 44, 45, 45]
       #0   1,  2,  3,  4,  5,  6,  7, 8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18 
v5_2= [45, 51, 50, 50, 41, 41, 47, 48, 51, 46, 45, 48, 47, 46, 46, 49, 48, 51, 44]

#además, agregar los 3dx y 3dy

v7_1= [68, 67, 67, 67, 68, 66, 67, 68, 67, 68, 68, 68, 67, 68, 66, 67, 68, 67, 68]
v7_2= [67, 69, 69, 69, 65, 68, 68, 67, 66, 65, 66, 67, 68, 66, 69, 69, 70, 69, 67]

v8_1= [69, 71, 71, 71, 70, 71, 71, 71, 71, 70, 70, 71, 71, 70, 71, 71, 71, 71, 70]
v8_2= [70, 70, 70, 70, 66, 67, 65, 64, 64, 64, 64, 64, 65, 65, 70, 70, 69, 70, 69]

v9_1= [62, 62, 62, 62, 61, 62, 62, 62, 62, 62, 61, 62, 62, 61, 62, 62, 62, 62, 61]
v9_2= [61, 68, 65, 64, 64, 64, 64, 65, 68, 61, 62, 65, 64, 64, 64, 64, 65, 68, 62]

v10_1= [66, 65, 66, 66, 67, 65, 66, 66, 65, 66, 67, 66, 66, 67, 65, 66, 66, 65, 66]
v10_2= [65, 66, 68, 68, 69, 70, 70, 70, 70, 67, 69, 70, 70, 69, 68, 68, 67, 66, 65]

#V = [(v1_1,v1_2,"Csp3-F2pz"),(v2_1,v2_2,"F3pz"),(v3_1,v3_2,"F3s"),(v4_1,v4_2,"F3dz"), (v5_1,v5_2,"F3py"),(v6_1,v6_2,"F3px"),
#       (v7_1,v7_2,"F3dxy"), (v8_1,v8_2,"F3dx2-y2"), (v9_1,v9_2,"F3dyz"), (v10_1,v10_2, "F3dxz") ]

V = [(v1_1,v1_2,"Csp3-F2pz"),(v2_1,v2_2,"F3pz"),(v3_1,v3_2,"F3s"),(v4_1,v4_2,"F3dz"), (v5_1,v5_2,"F3py"),(v6_1,v6_2,"F3px"),
       (v7_1,v7_2,"F3dxy"), (v8_1,v8_2,"F3dx2-y2"), (v9_1,v9_2,"F3dyz") ]


data = []
for ang in range(0,19,1):
    for i,j,k,l,m,n,o,p in itertools.combinations(V,8):
        mol, mo_coeff, mo_occ = extra_functions(molden_file=f"difluorethane_cc-pvdz_{ang*10}_Cholesky_PM.molden").extraer_coeff
        inv_prop = inverse_principal_propagator(mol=mol, mo_coeff=mo_coeff, o1=[o1[ang]], o2=[o2[ang]], 
                                                v1=[i[0][ang], j[0][ang], k[0][ang], l[0][ang], m[0][ang], n[0][ang],o[0][ang],p[0][ang]],
                                                v2=[i[1][ang], j[1][ang], k[1][ang], l[1][ang], m[1][ang], n[1][ang],o[1][ang],p[1][ang]])
        iajb_entropy = inv_prop.entropy_iajb_mixedstate
        
        data.append([ang*10, iajb_entropy, f'{i[2]}_{j[2]}_{k[2]}_{l[2]}_{m[2]}_{n[2]}_{o[2]}_{p[2]}', "Entropía"])

df = pd.DataFrame(data, columns=['angulo', 'Entanglement', 'Virtuals',  'Mutual Information'])
fig = px.line(df, x="angulo", y="Entanglement", animation_frame='Virtuals', color='Mutual Information',
       title="Entropy iajb Triplet in the Difluorethane (opt-HF) using combinations of 8 virtuals as antibondings, base cc-pvdz",
      )
fig.update_layout(    yaxis_title=r'Entrelazamiento' )

fig.write_html("entropy_iajb_triplet_difluorethane_8exc.html", include_mathjax='cdn')
#

data = []
for ang in range(0,19,1):
    for i,j,k,l,m,n,o,p in itertools.combinations(V,8):
        mol, mo_coeff, mo_occ = extra_functions(molden_file=f"difluorethane_cc-pvdz_{ang*10}_Cholesky_PM.molden").extraer_coeff
        inv_prop = inverse_principal_propagator(mol=mol, mo_coeff=mo_coeff, spin_dependence="singlet", 
                                            o1=[o1[ang]], o2=[o2[ang]], 
                                            v1=[i[0][ang], j[0][ang], k[0][ang], l[0][ang], m[0][ang], n[0][ang],o[0][ang],p[0][ang]],
                                            v2=[i[1][ang], j[1][ang], k[1][ang], l[1][ang], m[1][ang], n[1][ang],o[1][ang],p[1][ang]])
        iajb_entropy = inv_prop.entropy_iajb_mixedstate
        data.append([ang*10, iajb_entropy, f'{i[2]}_{j[2]}_{k[2]}_{l[2]}_{m[2]}_{n[2]}_{o[2]}_{p[2]}', "Entropía"])

df = pd.DataFrame(data, columns=['angulo', 'Entanglement', 'Virtuals',  'Mutual Information'])
fig = px.line(df, x="angulo", y="Entanglement", animation_frame='Virtuals', color='Mutual Information',
       title="Entropy iajb Singlet in the Difluorethane (opt-HF) using combinations of 8 virtuals as antibondings, base cc-pvdz",
      )
fig.update_layout(    yaxis_title=r'Entrelazamiento' )

fig.write_html("entropy_iajb_singlet_difluorethane_8exc.html", include_mathjax='cdn')

