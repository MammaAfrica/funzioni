import numpy as np
import math as mt

def corr_A_B(corr_data, corr_avg, n_corr_points, num_corr, A, B, integration_step):
    
    # <B(0)A(-t)>
  
    corr_data_0=corr_data.copy()
    corr_data[0]=A
    for i in range(1, num_corr):
          corr_data[i]=corr_data_0[i-1]

    # update the correlation functuion
    for i in range(num_corr):
        if integration_step >=i:
            corr_avg[i]=(corr_avg[i]*n_corr_points[i]+B*corr_data[i])/(n_corr_points[i]+1)
            n_corr_points[i]=n_corr_points[i]+1
    
    return corr_data, corr_avg, n_corr_points