# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:11:44 2020

@author: foobe
"""

#%
import os
def set_path():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

set_path()

#%%
def loadGraph(path):
    Graph = {}
    with open(path, 'r') as f:
        n, m = [int(x) for x in f.readline().split(' ')]
        for line in f.readlines():
            tail, head, cost = [int(x) for x in line.split(' ')]
            Graph[(tail,head)] = cost
    return Graph, n

#%%
path = 'g_test1.txt'

gtest, nt = loadGraph(path)

#%% Graph 1
path = 'g1.txt'

g1, n1 = loadGraph(path)

#%% Graph 2
path = 'g2.txt'

g2, n2 = loadGraph(path)

#%% Graph 3
path = 'g3.txt'

g3, n3 = loadGraph(path)
#Output smallest of apsp's for a given graph, Null if negative cycle
#Answer: Null, Null, -19, got it

#%% Floyd-Warshall, no space optimization
import numpy as np
#Array[k][row][column]
#For A[k], prints each row out 

def FW(graph, n):
    '''
    Computes smallest of all-pair shortest paths in graph

    Parameters
    ----------
    graph : Dictionary
        graph[(tail, head)] = [cost]
    n : Int
        number of vertices in graph g
        
    Returns
    -------
    None.

    '''
    A = np.zeros((n,n,n)) #n by n by n matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                A[0][i][j] = 0
            elif (i + 1,j + 1) in graph:
                A[0][i][j] = graph[(i + 1,j + 1)]
            else:
                A[0][i][j] = float('inf')
    for k in range(1, n):
        print(k)
        for i in range(n):
            for j in range(n):
                A[k][i][j] = min((A[k - 1][i][j], A[k-1][i][k] + A[k-1][k][j]))
    for i in range(n):
        if A[n - 1][i][i] < 0:
            print('A negative cycle exists')
            return None
    return A
            
#%% Space Optimized Floyd-Warshall

import numpy as np
#Array[k][row][column]
#For A[k], prints each row out 

def FW(graph, n):
    '''
    Computes smallest of all-pair shortest paths in graph

    Parameters
    ----------
    graph : Dictionary
        graph[(tail, head)] = [cost]
    n : Int
        number of vertices in graph g
        
    Returns
    -------
    None.

    '''
    A = np.zeros((2,n,n)) #n by n by n matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                A[0][i][j] = 0
            elif (i + 1,j + 1) in graph:
                A[0][i][j] = graph[(i + 1,j + 1)]
            else:
                A[0][i][j] = float('inf')
    for k in range(1, n):
        print(k)
        for i in range(n):
            for j in range(n):
                A[1][i][j] = min((A[0][i][j], A[0][i][k] + A[0][k][j]))
                A[0][i][j] = A[1][i][j]
                if i == j and A[1][i][j]:
                    print('A negative cycle exists')
                    return None
    '''
    for i in range(n):
        if A[1][i][i] < 0:
            print('A negative cycle exists')
            return None
    '''
    return A.min()

#%% Test all
graphs = [g1,g2,g3]
verts = [n1,n2,n3]

results = []
for i in range(3):
    print("graph ", i + 1)
    results.append(FW(graphs[i],verts[i]))
    
#%% Test All, not working

results = []

import time
import multiprocessing

if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target = FW, args = (graphs[i],verts[i]))
        processes.append(p)
        p.start()
    
    for process in processes:
        process.join()
        
    print('Time taken = {} seconds'.format(time.time() - starttime) )