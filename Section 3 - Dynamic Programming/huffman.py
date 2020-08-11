# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:41:08 2020

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
class CNode:
    def __init__(self, ID, weight, depth = 1):
        self._id = ID
        self.weight = weight
        self.depth = 1
        
    @classmethod
    def __merge__(cls, code1, code2):
        newWeight = code1.weight + code2.weight
        newID = str(code1._id) + "_" + str(code2._id)
        newDepth = code1.depth + 1
        obj = cls(newID, newWeight, newDepth)        
        return obj
        
    def __lt__(self, other):
        assert isinstance(other, CNode)
        return self.weight < other.weight
    
    def __hash__(self):
        return self._idS
    
    def __repr__(self):
        return ("ID: " + str(self._id) + " Weight: " + str(self.weight) +
                " Depth: " + str(self.depth))

#%% With Heaps
import heapq
'''
heappush(heap, item): insert
heappop(heap): extract min
heappushpop(heap, item): inserts item, then extracts min
heapify(x): transform x into heap in-place
heapreplace(heap, item): extracts min, then inserts item
'''

path = 'huffman.txt'

def loadHuff(path):
    Codes = []
    with open(path, 'r') as f:
        num = f.readline()
        i = 1
        for line in f.readlines():
            Codes.append(CNode(i, int(line)))
            i += 1
    heapq.heapify(Codes)
    return Codes

Codes = loadHuff(path)

#Correct Answer: 2493893
#%%
def SearchTime(tree):
    T = 0
    for node in tree:
        T += node.weight * node.depth
        