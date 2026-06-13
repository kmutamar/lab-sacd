import numpy as np
def euler(f,init,t,param):
    y=np.zeros((len(t),len(init)))
    y[0,:]=init
    dt=t[1]-t[0]
    for i in range(len(t)-1):
        y[i+1,:]=y[i,:]+dt*f(y[i,:],param)
    return y
