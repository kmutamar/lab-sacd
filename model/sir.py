import numpy as np
def sir(y,param):
    s=y[0];
    i=y[1];
    r=y[2];
    beta=param[0]
    gamma=param[1]
    ds=-beta*s*i
    di=beta*s*i-gamma*i
    dr=gamma*i
    return np.array([ds,di,dr])
