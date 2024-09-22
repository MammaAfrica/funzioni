import numpy as np
import math as mt

def force_calc(r, sigma, L_box, potential_type):
    if r>0:
        if potential_type=="harmonic":
            Force=-r
        if potential_type=="sin":
            Force=mt.sin(2*mt.pi/L_box*r)/100
    if r<=0:
        if potential_type=="harmonic":
            Force=-r
        if potential_type=="sin":
            Force=mt.sin(2*mt.pi/L_box*r)/100
    
    return Force

def update_velocity(r,v, friction ,time_step, Gamma, mass, 
                    potential_type, potential, sigma, L_box ):

    v=v-friction*v*time_step/mass
    noise=Gamma*np.random.normal(0, mt.sqrt(2*time_step), 1)[0]/mass
    v=v+noise

    Force=0

    if potential=="yes":
        Force=force_calc(r, sigma, L_box, potential_type)
        v=v+Force
    return v, noise, Force