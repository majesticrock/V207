import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
from uncertainties import umath

mg = 4.9528
mk = 4.4531 
rg = 1.5805 / 2 
rk = 1.5634 / 2 
Vg = 4/3 * np.pi * rg**3
Vk = 4/3 * np.pi * rk**3
rhog = mg / Vg *1000
rhok = mk / Vk *1000
print("Volumen große Kugel",  Vg)
print("Volumen kleine Kugel", Vk)
print ("Dichte Große Kugel:", rhog)
print ("Dichte Kleine Kugel:", rhok)
KK = 0.07640 /1000
eta = KK * (rhok - 998.20) * ufloat(11.67, 0.04)
print("Viskositaet: " , eta)
KG = eta /((rhog - 998.20) * ufloat(76.59, 0.08))
print("K groß: ", KG)