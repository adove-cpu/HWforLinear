from fitting_functions import *
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.stats import norm
data = np.loadtxt("tips.csv", delimiter=",", dtype=str)
bill = data[1:, 0].astype(np.float32)
tip = data[1:, 1].astype(np.float32)
pct_tip=t = data[1:, 6].astype(np.float32)
#graph 1
params, params_cov = scipy.optimize.curve_fit(linear, bill, tip)
slope = params[0]
intercept = params[1]
fig = plt.figure()
plt.scatter(bill, tip, label='Data')
plt.plot(bill, linear(bill, slope, intercept),label='Linear Line')
plt.legend(loc='best')
plt.xlabel("bill")
plt.ylabel("tips")
plt.show()
#equation 1
x_unit='dollars'
y_unit='dollars'
print(print_equations(slope,intercept,x_unit,y_unit))
#The equation of the line is: y= 0.1822 dollars/dollars x+ -0.2923 dollars
#graph 2
params, params_cov = scipy.optimize.curve_fit(linear, bill, pct_tip)
slope = params[0]
intercept = params[1]
fig = plt.figure()
plt.scatter(bill, pct_tip, label='Data')
plt.plot(bill, linear(bill, slope, intercept),label='Linear Line')
plt.legend(loc='best')
plt.xlabel("bill")
plt.ylabel("pct_tip")
plt.show()
#equation 2
z_unit='%'
print(print_equations(slope,intercept,x_unit,z_unit))
#The equation of the line is: y= 0.0488 %/dollars x+ 15.5096 %
