import numpy as np
K=68.39
def fungsi_error_zakat(a,data_t,data_f):
    f=np.sum((data_f-K*np.exp(a*data_t))**2)
    return f