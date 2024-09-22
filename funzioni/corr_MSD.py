import numpy as np
import math as mt

def MSD(corr_data_MSD, corr_avg_MSD, n_corr_points_MSD, num_corr_MSD, r, flag, integration_step, L_box):
    
    # update the data vector
    
    corr_data_MSD_0=corr_data_MSD.copy()
    corr_data_MSD[0]=r+2*L_box*flag
    for i in range(1, num_corr_MSD):
          corr_data_MSD[i]=corr_data_MSD_0[i-1]

    # update the correlation functuion

    for i in range(1, num_corr_MSD):
        if integration_step >=i:
            delta=corr_data_MSD[0]-corr_data_MSD[i]
            delta=delta**2
            corr_avg_MSD[i]=(corr_avg_MSD[i]*n_corr_points_MSD[i]+delta)/(n_corr_points_MSD[i]+1)
            n_corr_points_MSD[i]=n_corr_points_MSD[i]+1

    return corr_data_MSD, corr_avg_MSD, n_corr_points_MSD