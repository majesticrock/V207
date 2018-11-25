import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x +b
def h(x,a,b):
    return a * np.exp(-b/x)
werte = csv_read("csv/geradewerte.csv")
xdata = np.zeros(18)
ydata = np.zeros(18)
ignore = True
i=0

for values in werte:
    if(ignore):
        ignore = False
    else:
        ydata[i] = float(values[0])
        xdata[i] = float(values[1]) * 10**(-3)
        
        i+=1

x_line = np.linspace(0.003, 0.0034)
plt.plot(xdata, ydata, 'bx', label="Wertepaare")
popt1, pcov1 = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Ausgleichsgerade")
plt.xlabel(r"$\frac{1}{T}$ / K^{-1}")
plt.ylabel(r"$\ln (\eta)$")
print(popt1)
print(np.sqrt(np.diag(pcov1)))
plt.legend()
plt.tight_layout()
plt.savefig("build/gerade.pdf")
#print(np.exp(-12.55778199))