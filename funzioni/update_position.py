import numpy as np

def update_position(r,v,time_step, flag, boundary, L_box):
    # r is the position
    # v is the velocity
    # time step is the intwgration timestep
    
    r=r+v*time_step

    if boundary=="periodic":
         
        if r>L_box:
            r=r-2*L_box
            flag=flag+1
        
        if r<-L_box:
            r=r+2*L_box
            flag=flag-1
     
    return r, flag