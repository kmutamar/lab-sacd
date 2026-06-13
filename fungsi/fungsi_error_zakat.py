import numpy as np
def fungsi_error_zakat(a,K,data_t,data_f):
    f=np.sum((data_f-K*np.exp(a*data_t))**2)
    return f