import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# dN/dt=rN

#constants,initial conditions and time space
N_0=10 #initial pop
r=0.3 #pop growth rate per person

time_space=np.linspace(0,10,1001)

#the ode of the system/problem

def system_of_odes(y,t,r):
    N=y
    dndt=r*N
    return dndt

#solving ode using odeint 
#syntax: solution=odeint(func,y0,t,args)
solution=odeint(system_of_odes,y0=N_0,t=time_space,args=(r,))
print(solution)

plt.plot(time_space,solution)
plt.title("Population growth")
plt.xlabel("time")
plt.ylabel("Population")
plt.show()










