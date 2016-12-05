# -*- coding: utf-8 -*-
"""


"""

# %%



def state_eq(R, P=False, V=False, m=False, T=False):
    if P is False:
        P_=solve_P(V, m, T, R)
        return P_
    elif V is False:
        V_=solve_V(P, m, T, R)
        return V_
    elif m is False:
        m_ = solve_m(P, V, T, R)
        return m_
    elif T is False:
        T_ = solve_T(P, V, m, R)
        return T_
        
def solve_P(V, T, m, R):
    return m*R*T/V

def solve_V(P, m, T, R):
    return m*R*T/P
    
def solve_m(P, V, T, R):
    return P*V/R/T

def solve_T(P, V, m, R):
    return P*V/m/R

