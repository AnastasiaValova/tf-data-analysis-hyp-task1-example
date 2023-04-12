import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

def solution1(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.03
    stats, p_value = proportions_ztest(np.array([x_success, y_success]), np.array([x_cnt, y_cnt]), alternative = 'smaller')
    return p_value < alpha
