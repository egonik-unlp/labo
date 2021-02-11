#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 01:10:34 2021

@author: gonik
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir('/home/gonik/Documents/git/labo/2021')

df_data = pd.read_csv('contour2', sep = ';', thousands = '.', decimal = ',', index_col = 0).dropna()
df_columns = pd.read_csv('matriz3', sep = ';', thousands = '.', decimal = ',', index_col = 0)
df_data.columns = {i for i in df_columns.B}
fig = plt.figure(figsize = (15,10), dpi = 300 )
X = df_data[df_data < 1e6]
sns.heatmap(
    data = X.T,
    
    )

R = fig.gca()
plt.xlabel(r' $\lambda$ excitacion')
plt.ylabel(r' $\lambda$ emision')
R.set_ylim((0, 53.0))
R.set_xlim((0.0, 50))
plt.title('npsi @DMF')
plt.show()


'''
param = df_data.shape[0]

xx, yy = np.meshgrid(df_data.index, df_data.columns)
xx, yy = xx.reshape(param,-1), yy.reshape(param,-1)
zz = df_data.to_numpy()

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.plot_surface(xx,yy,zz)


plt.show()

plt.imshow(df_data)
'''