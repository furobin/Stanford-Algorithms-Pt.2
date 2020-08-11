# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:19:09 2020

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
path = 'tsp_small.txt'

class Point:
    def __init__(self, _id, x, y):
        self._id = _id
        self.x = x
        self.y = y
        
    def __repr__(self):
        return str(self._id)
    
    def __str(self):
        return str(self._id)
    
    def __eq__(self, other):
        assert isinstance(other, Point)
        return self._id == other._id
    
    def __hash__(self):
        return self._id

def loadtsp(path):
    points = []
    with open(path, 'r') as f:
        n = int(f.readline())
        i = 1
        for line in f.readlines():
            x, y = [float(x) for x in line.split(' ')]
            points.append(Point(i,x,y))
            i += 1
    return points, n

points, num = loadtsp(path)
#Answer = 8387.077130278542 maybe? 
#%%
import numpy as np

def dist(point1, point2):
    '''
    Returns Euclidiean distance between two points

    Returns
    -------
    float
        Euclidean distance between point 1 and point 2

    '''
    return np.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

#%%
from itertools import combinations 
from collections import defaultdict

def TSP(Points, N):
    Sub1 = defaultdict(dict)
    Sub1 = {'1': {1:0} }
    for m in range(2, N + 1):
        print(Sub1)
        print(m)
        for combination in combinations(points, m):
            if combination[0]._id != 1:
                break
            print(combination)
            key = '_'.join([str(x) for x in combination])
            Sub1[key] = {}
            for j in combination[1:]:
                excluded = [point for point in combination if point != j]
                print(excluded)
                testkey = '_'.join([str(k) for k in excluded])
                print(testkey)
                for k in excluded:
                    if k._id not in Sub1[testkey]:
                        continue
                    distance = dist(k,j)
                    case = Sub1[testkey][k._id] + distance
                    try:
                        if case < Sub1[key][j._id]:
                            Sub1[key][j._id] = case
                    except:
                        print('Create new entry')
                        Sub1[key][j._id] = case
    finalKey = '_'.join([str(p) for p in Points])
    minDist = min(dist(Points[0],Points[j - 1]) + Sub1[finalKey][j] for j in Sub1[finalKey])
    return Sub1, minDist