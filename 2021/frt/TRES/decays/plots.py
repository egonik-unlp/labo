import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir('/home/gonik/Documents/git/labo/2021/frt/TRES/decays')

dataframes = [(int(file[6:-4])  ,pd.read_csv(file, sep= '\t')) for file in os.listdir() if 'decay' in file]



for i in dataframes:
    plt.plot(dataframes[1][1].Chan, i[1].Decay)
    plt.xlim((100, 300))
    
    
tablas = pd.concat([nodo[1].Decay for nodo in dataframes], axis = 1)
channels = dataframes[1][1].Chan
lambdas = [int(nodo[0]) for nodo in dataframes]
lambdas.sort()
tabla = pd.concat([channels, tablas], axis = 1)
tablas.columns = lambdas