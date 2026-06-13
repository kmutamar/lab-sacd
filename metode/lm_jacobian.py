import numpy as np
def func_lm_jacobian(residu_lm,datat, datay, K, a, h):
    t = np.asarray(datat)
    J = np.zeros((len(t),2))
    J[:,0] = -np.exp(a*t)
    J[:,1] = -K*t*np.exp(a*t)
    return J    