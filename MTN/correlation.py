# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:01:04 2019

@author: Hossein
"""

import scipy as sp
import numpy as np
import pandas as pd
import xlrd
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt

loc  =  'C:\\Users\\Hossein\\Desktop\\MTN\\R3.xlsx'
loc1 = 'C:\\Users\\Hossein\\Desktop\\MTN\\R3-1.xlsx'
loc2 = 'C:\\Users\\Hossein\\Desktop\\MTN\\R3-U2100.xlsx'
loc3 = 'C:\\Users\\Hossein\\Desktop\\MTN\\R3-U900.xlsx'
#df = pd.read_csv(loc,encoding='utf-8')
wb  = xlrd.open_workbook(loc)
wb1 = xlrd.open_workbook(loc1)
wb2 = xlrd.open_workbook(loc2)
wb3 = xlrd.open_workbook(loc3)

sheet  = wb.sheet_by_index(1)
sheet1 = wb1.sheet_by_index(0)# 3G
sheet2 = wb1.sheet_by_index(0)# 3G - U2100
sheet3 = wb1.sheet_by_index(0)# 3G - U900


### test
sheet.cell_value(2, 2)
sheet1.cell_value(2, 2)
print(sheet.ncols)
print(sheet1.ncols)
#%% Definition

KPI= {}

kpi_2G = {}
kpi_3G = {}
kpi_3G_u2100 = {}
kpi_3G_u900 = {}

num1 = sheet.ncols -2
num2 = sheet.nrows -1

for i in range(2,num1): 
    print(sheet.cell_value(0, i))
    kpi_2G[sheet.cell_value(0, i)] = []
    for j in range(1,sheet.nrows):
        
        kpi_2G[sheet.cell_value(0, i)].append(sheet.row_values(j)[i])
        
        
for i in range(2,num1): 
    print(sheet1.cell_value(0, i))
    kpi_3G[sheet1.cell_value(0, i)] = []
    for j in range(1,sheet1.nrows):
        
        kpi_3G[sheet1.cell_value(0, i)].append(sheet1.row_values(j)[i])
        
for i in range(2,num1): 
    print(sheet2.cell_value(0, i))
    kpi_3G_u2100[sheet2.cell_value(0, i)] = []
    for j in range(1,sheet2.nrows):
        
        kpi_3G_u2100[sheet2.cell_value(0, i)].append(sheet2.row_values(j)[i])
        
for i in range(2,num1): 
    print(sheet3.cell_value(0, i))
    kpi_3G_u900[sheet3.cell_value(0, i)] = []
    for j in range(1,sheet3.nrows):
        
        kpi_3G_u900[sheet3.cell_value(0, i)].append(sheet3.row_values(j)[i])

#%%       Correlation coefficinet 
        
corr1 = {} # correlation DCR vs 2G kpis
corr2 = {} # correlation DCR vs 3G kpis
corr3 = {} # correlation DCR vs 3G kpis U2100
corr4 = {} # correlation DCR vs 3G kpis U900

keyss_2G = []
for i in kpi_2G.keys():
    
    keyss_2G.append(i)
    
    
keyss_3G = []
for i in kpi_3G.keys():
    
    keyss_3G.append(i)
    

keyss_3G_u2100 = []
for i in kpi_3G_u2100.keys():
    
    keyss_3G_u2100.append(i)
    
keyss_3G_U900 = []
for i in kpi_3G_u900.keys():
    
    keyss_3G_U900.append(i)
    
    
for i in keyss_2G:
    
    corr1[i] = sp.stats.pearsonr(kpi_2G[i],kpi_2G[keyss_2G[25]])
    
for i in keyss_3G:
    
    corr2[i] = sp.stats.pearsonr(kpi_3G[i],kpi_2G[keyss_2G[25]])    
    
    
for i in keyss_3G_u2100:
    
    corr3[i] = sp.stats.pearsonr(kpi_3G_u2100[i],kpi_2G[keyss_2G[25]]) 
    
for i in keyss_3G_U900:
    
    corr4[i] = sp.stats.pearsonr(kpi_3G_u900[i],kpi_2G[keyss_2G[25]]) 
    
l = 0 
   
plot_2G = kpi_2G[keyss_2G[25]]

plot_2G = [ (i-np.mean(plot_2G))/np.var(plot_2G) for i in plot_2G]

for i in keyss_3G_U900:
    
    
    plot_3G = kpi_3G_u900[i]
    plot_3G = [(i-np.mean(plot_3G))/np.var(plot_3G) for i in plot_3G]
    l =+ 1
    plt.figure(l)
    
    plt.plot(plot_3G, 'r')
    plt.plot(plot_2G, 'b')
    
    
    
    
    
    
    
    
    
    
    
