# -*- coding: utf-8 -*- Not functional
"""
Created on Sun Jul 19 17:33:22 2020

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
    return points

Points = loadtsp(path)
#Answer = 26442
#%%
path = 'tsp.txt'

Points = loadtsp(path)
#%%
from math import sqrt

def dist(point1, point2):
    '''
    Returns Euclidiean distance between two points

    Returns
    -------
    float
        Euclidean distance between point 1 and point 2

    '''
    return sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

#%%
from itertools import combinations

def findSubs(Points, Cardinality):
    '''
    Finds combinations of points up to a certain cardinality; stores combination as keys

    Parameters
    ----------
    n : Int
        Number of points in total    
    
    Cardinality : Int

    Returns
    -------
    Subs : Dict
        keys = 'id1_id2_id3...etc'
        IDs are sorted
        
    '''
    Subs = {}
    for i in range(1, Cardinality + 1):
        for combination in combinations(Points, i):
            key = '_'.join([str(x) for x in combination])
            Subs[key] = float('inf')
    return Subs

#%%
def findSubs(Points, Cardinality):
    '''
    Find combinations of points with a certain cardinality; stores combinations as keys
    Assumes starting point is point 1.

    Parameters
    ----------
    n : Int
        Number of points in total    
    
    Cardinality : Int

    Returns
    -------
    Subs : Dict
        keys = 'id1_id2_id3...etc'
        IDs are sorted, id1 always = starting vertex id. 
        
    '''
    
    Subs = {}
    for combination in combinations(Points, Cardinality):
        if str(combination[0]) != '1':
            break
        key = '_'.join([str(x) for x in combination])
        Subs[key] = float('inf')
    return Subs
#%%
def TSP(Points):
    n = len(Points)
    Subs = {}
    Subs['1'] = 0
    def SubsUpdate(Cardinality):
        for combination in combinations(Points, Cardinality):
            if str(combination[0]) != '1':
                break
            IDs = [x._id for x in combination]
            #print(IDs)
            key = '_'.join([str(x) for x in combination])
            #print(key)
            for j in combination[1:]:
                excluded = [point for point in combination if point != j]
                #print(j)
                #print(excluded)
                dists = [dist(j, p2) for p2 in excluded]
                testkey = '_'.join([str(num) for num in excluded])
                #print(testkey)
                cases = [Subs[testkey] + dist for dist in dists]
                Subs[key] = min(cases)
    for m in range(2, n + 1):
        SubsUpdate(m)
    lastkey = '_'.join([str(point) for point in Points])
    #print(lastkey)
    minDist = min([Subs[lastkey] + dist(Points[0], j) for j in Points if j != Points[0]])
    return Subs, minDist

test, minDist = TSP(Points)
#%%
def SubsUpdate(Points, Cardinality):
    for combination in combinations(Points, Cardinality):
        if str(combination[0]) != '1':
            break
        IDs = [x._id for x in combination]
        print(IDs)
        key = '_'.join([str(x) for x in combination])
        print(key)
        for j in combination[1:]:
            excluded = [point for point in combination if point != j]
            print(j)
            print(excluded)
            dists = [dist(j, p2) for p2 in excluded]
            testkey = '_'.join([str(num) for num in excluded])
            print(testkey)
            cases = [Subs[testkey] + dist for dist in dists]
            Subs[key] = min(cases)

    
#%%
for combination in combinations(Points, 3):
    if str(combination[0]) != '1':
        break
    IDs = [x._id for x in combination]
    print(IDs)
    key = '_'.join([str(x) for x in combination])
    print(key)
    for j in combination[1:]:
        excluded = [point for point in combination if point != j]
        print(j)
        print(excluded)
        dists = [dist(j, p2) for p2 in excluded]
        testkey = '_'.join([str(num) for num in excluded])
        print(testkey)
        cases = [Subs[testkey] + dist for dist in dists]
        Subs[key] = min(cases)