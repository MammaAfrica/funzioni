
import numpy as np
import math as mt


def inizialization(r0, v0, num_corr, num_corr_MSD):
    
    # inizialization of velocities and positions
    r=r0
    v=v0

    # inizialization of the correlate function
    corr_data=np.zeros(num_corr)
    n_corr_points=np.zeros(num_corr)
    corr_avg=np.zeros(num_corr)

    corr_data_MSD=np.zeros(num_corr_MSD)
    corr_avg_MSD=np.zeros(num_corr_MSD)
    n_corr_points_MSD=np.zeros(num_corr_MSD)

    flag=0


    return r, v, corr_data, corr_avg, n_corr_points, corr_data_MSD, corr_avg_MSD, n_corr_points_MSD, flag
