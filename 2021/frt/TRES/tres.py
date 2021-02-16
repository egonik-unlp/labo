#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import pandas as pd
import numpy as np
import csv
import datetime
from celluloid import Camera
import sys 
import os
import matplotlib.pyplot as plt

def das_parser(das_file):
  with open(das_file, 'r' ) as file:
      lines = csv.reader(file, delimiter = '\r')
      for i in range(3):
          next(lines)
      k = 1
      while k < 19:
          with open(f'Decay {625 + 5*k}.csv', 'w') as f: 
              n = 0 
              while n <= 4096:    
                  line = next(lines)
                  f.write(','.join(line))
                  f.write('\n')
                  n += 1
              for i in range(5):
                  next(lines)
              n = 0
          k += 1
          

def main(file_input, exts, max_em, muestra, filename):
    das_parser(file_input)
    dataframes = [(int(file[6:-4])  ,pd.read_csv(file, sep= '\t')) for file in os.listdir() if 'Decay' in file]
    
    tablas = pd.concat([nodo[1].Decay for nodo in dataframes], axis = 1)
    idx_ns = dataframes[1][1].Chan * 0.1097394
    tablas.index = idx_ns
    lambdas = [int(nodo[0]) for nodo in dataframes]
    lambdas.sort()
    tablas.columns = lambdas
    
    taus = [i for i in tablas.index.values if i > exts[0] and i < exts[1]]
    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (20,10))
    camera = Camera(fig)
    
    for tau in taus:
      emm_int = tablas.loc[tau,:]
      ax[0].plot(tablas[max_em].loc[taus[0]:taus[-1]] , c = 'black')
      ax[0].set_title(f'Fluorescencia resuelta en el tiempo de {muestra}' r' para $\lambda_{em} $ = 650 nm ', fontsize = 16)
      ax[0].set_xlabel(r'$\tau$ (ns)', fontsize = 16)
      ax[0].axvline(tau)
      ax[1].plot(tablas.columns,emm_int, c = 'g')
      ax[1].set_title(f'Espectro de emision de {muestra} ' r'para distintos $\tau$', fontsize = 16)
      ax[1].set_xlabel(r'$\lambda_{em} (nm)$', fontsize = 16)
      ax[1].legend([rf'$\tau = {tau:0.2f}$ ns'], fontsize = 14)
      camera.snap()
    
    len_idx = len(idx_ns)
    
    animation = camera.animate()
    animation.save(f'{filename}_tres.gif', writer = 'pillow')
#%% Input Block
if __name__ == '__main__': 
    le = int(input('tau inferior: '))
    he = int(input('tau superior: '))
    exts = [le,he]
    max_em = int(input('máximo de emisión: '))
    filename = input('nombre de archivo de salida: ')
    muestra = input('sustancia de muestra: ')
    main(sys.argv[1], exts, max_em, muestra, filename)
    
    
