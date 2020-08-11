# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:17:50 2020

@author: foobe
"""

#%
import os
def set_path():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

set_path()

#%% File Loading Function
def loadCons(path):
    with open(path, 'r') as f:
        n = int(f.readline())
        cons = []
        for line in f.readlines():
            c1, c2 = [int(x) for x in line.split(' ')]
            cons.append((c1,c2))
    return n, cons

#%% 1st
n1, cons1 = loadCons('2sat1.txt')

#%% 2nd
n2, cons2 = loadCons('2sat2.txt')

#%% 3rd
n3, cons3 = loadCons('2sat3.txt')

#%% 4th
n4, cons4 = loadCons('2sat4.txt')

#%% 5th
n5, cons5 = loadCons('2sat5.txt')

#%% 6th
n6, cons6 = loadCons('2sat6.txt')

#%% Test
nt, const = loadCons('2sat_test1.txt')

#%%
def readCons(x, cons):
    flips = [] #stores indices of pairs of unsuccessful vertices
    for con in cons:
        #print(con)
        varis = []
        for i in con: 
            if i < 0:
                varis.append(x[abs(i) - 1] ^ 1) #flips value of variable
            else:
                varis.append(x[i - 1])
        #print(varis)
        if not any(varis):
            flips.append(con)
    return flips
        
        
#%% Slow Implementation
import numpy as np

def twoSat(n, cons):
    for i in range(int(np.log2(n))):
        x = np.random.randint(2, size = n)
        for j in range(int(2 * n **2 )):
            flips = readCons(x, cons)
            if not flips: #flips is empty, all constraints met
                return 1
            else:
                toflip = flips[np.random.randint(len(flips))]
                index = np.random.choice(toflip)
                x[abs(index) - 1] = x[abs(index) - 1] ^ 1 #flips value
    return 0

#%%
Constraints = [cons1,cons2,cons3,cons4,cons5,cons6]
Lengths = [n1,n2,n3,n4,n5,n6]

def tests(lengths, constraints):
    results = []
    for i in range(len(constraints)):
        print('Running File:', i + 1)
        results.append(twoSat(lengths[i], constraints[i]))
    return results

results = tests(Lengths, Constraints)