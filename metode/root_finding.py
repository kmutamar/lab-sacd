import numpy as np
import timeit

#--- metode Newton
def newton(f,df,init,itmax=1000,tolmax=1e-10):
    awal=timeit.default_timer()
    x=np.zeros(itmax)
    x[0]=init
    for i in range(itmax-1):
        x[i+1]=x[i]-f(x[i])/df(x[i])
        if np.abs(df(x[i+1]))< tolmax or (
            np.abs(f(x[i+1]))<tolmax):
                iter=i+1
                break
    return [iter,x[:i+2],timeit.default_timer()-awal]


