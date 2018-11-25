import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
from uncertainties import umath

t = ufloat(11.666999999999998, 0.04139377301532735)
eta = (7.64 * 10**(-8)) * (2368.67 - 998) * t
print(eta)
tgr = ufloat (76.588, 0.07663477597598198)
K = eta / ((2567.56 - 998) * tgr)
print(K)
i = 0
tv = [76.62, 76.59, 63.00, 62.71, 59.14, 59.58, 54.88, 54.91, 51.14, 50.10, 47.96, 47.09, 44.73, 44.32, 40.15, 40.65, 38.52, 38.64]
fl = [997.77, 997.77, 995.34, 995.34, 994.37, 994.37, 992.59, 992.59, 991.03, 991.03, 989.36, 998.36, 987.58, 987.58, 985.20, 985.20, 982.15, 982.15 ]
e = unp.uarray(np.zeros(18), np.zeros(18))
for values in tv:
    e[i] = K * (2567.56 - fl[i]) * tv[i]
    #print(math.log(e[i].nominal_value)) 
    i=i+1
i =0     
T = [295.15, 295.15, 304.15, 304.15, 307.15, 307.15, 312.15, 312.15, 316.15, 316.15, 320.15, 320.15, 324.15, 324.15, 329.15, 329.15, 334.15, 334.15]

for values in T:
    print(1/T[i])
    i= i+1

u = ufloat(0.000622  , 0.000002)
re = (998* 2*0.00765*0.1)/(38.64 * u)
print(re) 



