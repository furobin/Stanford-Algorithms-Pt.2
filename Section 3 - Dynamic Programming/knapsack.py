# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:40:07 2020

@author: foobe
"""

#%
import os
def set_path():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

set_path()

#%% Item and load function
import collections

Item = collections.namedtuple('Item', ('value','weight'))

def loadKnap(path):
    Knap = []
    with open(path, 'r') as f:
        knapsize, n = [int(x) for x in f.readline().split(' ')]
        minWeight = float('inf')
        for line in f.readlines():
            val, weight = [int(x) for x in line.split(' ')]
            if weight < minWeight:
                minWeight = weight
            Knap.append(Item(val, weight))
    return knapsize, minWeight, Knap
#%% Smaller Knapsack

path = 'knapsack1.txt'
size1, min1, Knap1 = loadKnap(path)
#Correct Answer 1: 2493893, Got It

#%% Larger Knapsack

path = 'knapsack2.txt'
size2, min2, Knap2 = loadKnap(path)
#Correct Answer 2: 4243395, Got it although slow

#%% KnapTest
path = 'knaptest.txt'
tsize, tmin, tKnap = loadKnap(path)

#%% Test 2
path = 'knaptest2.txt'
tsize, tmin, tKnap = loadKnap(path)

#%% Test 3
path = 'knaptest3.txt'
tsize, tminn, tKnap = loadKnap(path)

#%% Knapsack, unoptimized

def Knapsack(size, minWeight, Knap):
    x = range(minWeight, size + 1) #Weights from minWeight to size
    n = len(Knap) #number of items
    A = [[0] * (size + 1) for item in range(n)] #2D array storing values, A[item][weight], weight  to size
    for item in range(0, n):
        #print('Item: ', item)
        for weight in x:
            #print('Weight Allowed: ', weight)
            wi = Knap[item].weight
            if wi <= weight:
                #print ('wi < weight')
                new = max((A[item - 1][weight], A[item-1][weight - wi] + Knap[item].value))
                #print(new, "assigned")
                A[item][weight] = new
            else: #wi > weight:
                #print('taking left value')
                A[item][weight] = A[item - 1][weight]
    return A
        
#%% Knapsack, optimized, 2nd draft; Correct 
import copy

def OKnapsack(size, Knap):
    n = len(Knap)
    Knap = sorted(Knap, key = lambda x: x.weight)
    #2 dictionaries with weights for keys
    A = dict.fromkeys(list(range(size + 1)), 0) #Seen Best
    B = dict.fromkeys(list(range(size + 1)), 0) #Considered Item
    for i in range(0, n):
        #print(A)
        item = Knap[i]
        print('Item #: ', i, item) 
        for weight in range(size, item.weight - 1, -1):
            B[weight] = A[weight - item.weight] + item.value
            if B[weight] > A[weight]:
                A[weight] = B[weight]
    return A

#%% Knapsack, optimized, 2nd draft testing; exists logic error, stick with first one. 
import copy

def OKnapsack(size, Knap):
    n = len(Knap)
    Knap = sorted(Knap, key = lambda x: x.weight)
    #2 dictionaries with weights for keys
    A = dict.fromkeys(list(range(size + 1)), 0) #Seen Best
    B = dict.fromkeys(list(range(size + 1)), 0) #Considered Item
    for i in range(0, n):
        #print(A)
        item = Knap[i]
        #print('Item #: ', i, item)
        for weight in range(size, item.weight - 1, -1):
            B[weight] = A[weight - item.weight] + item.value
            if B[weight] > A[weight]:
                A[weight] = B[weight]
            else:
                break
    return A
#%%
import time
from statistics import mean

print("Time for unoptimized")
Times = []
for i in range(20):
    t1 = time.time() 
    Knapsack(size1, min1, Knap1)
    t2 = time.time()
    Times.append(t2 - t1)
print("Avg of 20: ", mean(Times))

#%%
import time
from statistics import mean 

print("Time for optimized")
Times = []
for i in range(20):
    t1 = time.time()
    OKnapsack(size1, Knap1)
    t2 = time.time()
    Times.append(t2 - t1)
print("Avg of 20: ", mean(Times))