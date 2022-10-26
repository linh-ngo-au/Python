# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:48:48 2022

@author: Linh
"""

# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
 
from lifelines import KaplanMeierFitter
from lifelines.utils import median_survival_times
from lifelines.statistics import pairwise_logrank_test



# Load the telco silver table
phuong = pd.read_excel('C:\\Users\\Linh\\Downloads\\Phuong_master.xlsx', sheet_name="Version2")

kmf = KaplanMeierFitter()

kmf.fit(phuong['Time'],phuong['Progress'])

T=phuong['Time']

C=phuong['Progress']

kmf.plot(title='Kaplan-Meier Survival Curve')

print('Median survival time is', kmf.median_survival_time_)

print()

# Helper function for plotting Kaplan-Meier curves at the covariate level
def plot_km(col):
    plt.clf()
    ax = plt.subplot(111)
    for r in phuong[col].unique():
        ix = phuong[col] == r
        kmf.fit(T[ix], C[ix],label=r)
        kmf.plot(ax=ax)
    plt.show()
        
phuong['Gender']=phuong['Sex'].map({1: "Female", 0: "Male"})
plot_km('Gender')


phuong['Age_60'] = np.where(phuong['Age_diagnosed'] >=60, 1, 0)
phuong['Age_60'] = phuong['Age_60'].map({1: "Age>=60", 0: "Age<60"})
plot_km('Age_60')


# Helper function for printing out Log-rank test results

def print_logrank(col):
  print()
  log_rank = pairwise_logrank_test(phuong['Time'], phuong[col], phuong['Progress'])
  print('Log-rank test for', col, 'is')
  print()
  print(log_rank.summary)
  return log_rank.summary

print_logrank('Gender')


