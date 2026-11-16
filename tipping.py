from fitting_functions import *
import matplotlib.pyplot as plt
import scipy
import numpy as np
data = np.loadtxt("tips.csv", delimiter=",", dtype=str)
from scipy.stats import norm
data = np.loadtxt("tips.csv", delimiter=",", dtype=str)
print (data)
x= data[1:, 0].astype(np.float32)
y= data[1:,1].astype(np.float32)
print("y = ", y)
print("x = ", x)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
x_unit="dollars"
y_unit="dollars"
print_equation(slope, intercept, y_unit, x_unit)
#The equation of the line is: y= 0.1822 dollars/dollars x +  -0.2923 dollars
x= data[1:, 0].astype(np.float32)
y= data[1:,-1].astype(np.float32)
print("y = ", y)
print("x = ", x)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
#exercise 1
x_unit="dollars"
y_unit="%"
print_equation(slope, intercept, y_unit, x_unit)
#The equation of the line is: y= 0.0488 dollars/% x +  15.5096 %
fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("Bill (dollars)") #change the units as appropriate
plt.ylabel("PctTip (%)")  #change the units as appropriate
plt.show()

