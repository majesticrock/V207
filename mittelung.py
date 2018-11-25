import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content
werte = csv_read("csv/constT.csv")
datak = np.zeros(10)
datag = np.zeros(10)
ignore = True
i = 0

for values in werte:
    if(ignore):
        ignore = False
    else:
        datak[i] = float(values[0])
        datag[i] = float(values[1])
        i = i+1

k = np.mean(datak)    
dk = np.std(datak, ddof = 1) / np.sqrt(len(datak)) 
g = np.mean(datag)    
dg = np.std(datag, ddof = 1) / np.sqrt(len(datag))    
print(k, dk)
print(g, dg)