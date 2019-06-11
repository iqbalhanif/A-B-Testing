# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##import 
import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import t 

##read data
data = pd.read_csv("file name", sep = ";")

##do calculation to get conversion rate (treatment/a or control/b)

##P-Value Function
def get_pvalue(con_conv, test_conv, con_size, test_size,):
    lift = - abs(test_conv - con_conv)
    scale_one = con_conv * (1 - con_conv) * (1 / con_size)
    scale_two = test_conv * (1 - test_conv) * (1 / test_size)
    scale_val = (scale_one + scale_two)**0.5
    t_test = abs(lift / scale_val)
    t_stat = t.ppf(1 - 0.025, df=con_size + test_size - 2)
    p_value = 2 * scipy.stats.norm.cdf(lift, loc = 0, scale = scale_val )
    return (t_test, t_stat, p_value)

##test
get_pvalue(a,b,na,na) ##ganti a,b,na,nb disesuaikan

##description
##a = converision rate a
##a = converision rate b
##na = number of sample a
##nb =  number of sample b

##Confidence Interval Fucntion
def get_ci(lift, alpha, sd):
    val = abs(scipy.stats.norm.ppf((1 - alpha)/2))
    lwr_bnd = lift - val * sd
    upr_bnd = lift + val * sd
    return_val = (lwr_bnd, upr_bnd)
    return(return_val)
    
##test
get_ci(a-b,alpha, sd) ##ganti a-b, alpha, sd disesuaikan
##description
##a-b = selisih antar converision rate a dan b
##alpha = taraf kealasahan / type error I
##sd = standard deviation