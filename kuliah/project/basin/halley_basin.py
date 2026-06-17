# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:17:09 2019

@author: khozin
"""
# import yang diperlukan
import numpy as np
import timeit
def halley_basin_func(f,df,d2f,a,b,n,tolmax,itmax):
    mulai=timeit.default_timer()    
    x=np.linspace(a,b,n)
    y=np.linspace(a,b,n)
    Rex,Imx=np.meshgrid(x,y)
    xold=Rex+1j*Imx
    # Menghitung xnew dengan Newton
    for i in range(0,itmax):
        xnew=xold-2*f(xold)*df(xold)/(2*df(xold)**2-f(xold)*d2f(xold))
        xold=xnew
    return xold,timeit.default_timer()-mulai

