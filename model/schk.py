#[Gamma,kappa,mu,omega,beta,u]
import numpy as np
def schk(y,param):
    s=y[0];
    c=y[1];
    h=y[2];
    Gamma=param[0]
    kappa=param[1]
    mu=param[2]
    omega=param[3]
    beta=param[4]
    u=param[5]
    #----------------
    ds=Gamma-(1-u)*kappa*c*s-mu*s+omega*h
    dc=(1-u)*kappa*c*s-beta*c-mu*c
    dh=beta*c-(mu+omega)*h
    return np.array([ds,dc,dh])
