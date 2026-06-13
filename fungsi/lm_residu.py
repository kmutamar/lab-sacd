import numpy as np

def func_lm_residu(datat, datay, K, a):

    t = np.asarray(datat).reshape(-1,1)
    d = np.asarray(datay).reshape(-1,1)

    res = d - K*np.exp(a*t)

    return res