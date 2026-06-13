import numpy as np
import timeit
def dichotomous_pon(fungsi_error,init,tolmax,data_t,data_f,K):
    awal=timeit.default_timer()
    epsilon=1e-10
    itmax=int(1e2)
    a,b=init
    for i in range(itmax):
        an=0.5*(a+b-epsilon)
        bn=0.5*(a+b+epsilon)
        f=[fungsi_error(an,K,data_t,data_f),fungsi_error(bn,K,data_t,data_f)]
        if f[0]<f[1]:
            b=bn
        elif f[0]>f[1]:
            a=an
        if np.abs(a-b)<tolmax:
            break
        #print('%2d %3.5f %3.5f %3.5f \n' % (i,a,b,np.abs(a-b)))
    return [an,bn,f,timeit.default_timer()-awal] 