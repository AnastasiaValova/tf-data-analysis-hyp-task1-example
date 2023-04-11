import pandas as pd
import numpy as np


chat_id = 225497605 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    a = x_cnt*((x_success+y_success)/(x_cnt+y_cnt))
    b = y_cnt*((x_success+y_success)/(x_cnt+y_cnt))
    X=((x_success-a)/a)**2 + ((y_success-b)/b)**2
   
    if X < scipy.stats.chi2.ppf(0.03, 1):
        return True
    else:
        return False
