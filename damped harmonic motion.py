import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# Damped harmonic motion

#constants,initial conditions and time space
ic=[1,0.5] #initial displacement,initial velocity
c=0.7 #damping constant
k=10 #spring constant
m=1 #mass


time_space=np.linspace(0,10,1001)

#the ode of the system/problem

def system_of_odes(y,t,c,m,k):
    x,x_dot=y
    x_ddot=-c/m *x_dot -k/m *x
    return x_dot, x_ddot
    
    

#solving ode using odeint 
#syntax: solution=odeint(func,y0,t,args)
solution=odeint(system_of_odes,y0=ic,t=time_space,args=(c,m,k))
x_sol=solution[:,0]
x_dot_sol=solution[:,1]
print(x_sol)
print(x_dot_sol)

plt.plot(time_space,x_sol,label="displacement")
plt.plot(time_space,x_dot_sol,label="velocity")
plt.title("Damped harmonic motion")
plt.xlabel("time")
plt.legend()
plt.show()











