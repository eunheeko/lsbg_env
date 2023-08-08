import numpy as np

def bulge(r, Sig_e, r_e, n):
    
    k = 1.9992 * n - 0.3271
    func = Sig_e * np.exp(-k * ( (r/r_e)**(1/n) - 1 ))

    return func

def disk(r, Sig_0, r_d):

    func = Sig_0 * np.exp(-r/r_d)

    return func