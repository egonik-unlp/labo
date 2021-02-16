import pandas as pd
import numpy as np
import csv
import os

os.chdir('/home/gonik/Documents/git/labo/2021/frt/TRES')

with open('ext.txt', 'r' ) as file:
    lines = csv.reader(file, delimiter = '\r')
    for i in range(3):
        next(lines)
    k = 1
    while k < 19:
        with open(f'decay {625 + 5*k}.csv', 'w') as f: 
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

