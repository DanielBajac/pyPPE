import os
import sys
module_path = os.path.abspath(os.path.join('..'))

if module_path not in sys.path:
    sys.path.append(module_path)


from src.help_functions import extra_functions
from src.cloppa import Cloppa
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mol_loc, mo_coeff_loc, mo_occ_loc = extra_functions(molden_file=f"H2O2_mezcla_100.molden").extraer_coeff
mol_H2O2 = '''
O1   1
O2   1 1.45643942
H3   2 0.97055295  1 99.79601616
H4   1 0.97055295  2 99.79601616  3 100
'''

viridx = np.where(mo_occ_loc==0)[0]
occidx = np.where(mo_occ_loc==2)[0]
full_M_obj = Cloppa(
    mol_input=mol_H2O2,basis='6-31G**',
    mo_coeff_loc=mo_coeff_loc, mol_loc=mol_loc, #vir=viridx, occ=occidx,
    mo_occ_loc=mo_occ_loc)

full_M_obj.kernel





