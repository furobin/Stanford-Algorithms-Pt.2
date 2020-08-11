#%%
import os
def set_path():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

set_path()
#%%
import collections
from python_algorithms.basic import union_find
import copy
import itertools

'''
UF: 
    find(self,p): finds set identifier of item p
    count(self): returns number of items, basically number of clusters
    connected(self, p q): checks if p and q in same cluster
    union(self, p, q): combines sets containing p and q
'''

#%%
path = 'hamming.txt'

Nodes = {}
Node = collections.namedtuple('Node', ('bstring', 'bits'))

with open(path, 'r') as f:
    n, bits = [int(x) for x in f.readline().strip().split(' ')]
    i = 0
    for line in f.readlines():
        bstring = line[:-2].replace(' ','')
        bits = bytearray([int(x) for x in list(nodebits)])
        Nodes[i] = Node(bstring, bits)
        i += 1

#%% Without implementing all 200,000 nodes due to repeats
path = 'hamming.txt'

def loadNodes(path):
    with open(path, 'r') as f:
        Nodes = {}
        n, bitlen = [int(x) for x in f.readline().strip().split(' ')]
        for line in f.readlines():
            bstring = line[:-2].replace(' ','')
            bits = bytearray([int(x) for x in list(bstring)])
            Nodes[bstring] = bits
    return Nodes

Nodes = loadNodes(path)
#2nd Part Answer: 6118, got it

#%% Includes Node ID
path = 'hamming.txt'

def loadNodes(path):
    with open(path, 'r') as f:
        Nodes = {}
        n, bitlen = [int(x) for x in f.readline().strip().split(' ')]
        i = 0
        for line in f.readlines():
            bstring = line[:-2].replace(' ','')
            bits = bytearray([int(x) for x in list(bstring)])
            if bstring not in Nodes:
                Nodes[bstring] = (bits, i)
                i += 1
    return Nodes

NodesID = loadNodes(path)

#%%
def HammingLim(node, dist = 2):
    '''
    Find bytearrays that are within the distance from imput node.

    Parameters
    ----------
    node : bytearray()
        Node with associated bytearray
    dist : INT, optional
        DESCRIPTION. The default is 2.

    Returns
    -------
    List of valid bytearrays within the distance
    '''
    indices = itertools.combinations(range(len(node)), dist)
    valid = []
    for flip in indices:
        ref = copy.copy(node)        
        for i in flip:
            ref[i] ^= 1
            valid.append(ref)
    return valid
            
#%%
def HammingCluster(nodes, dist = 2):
    '''
    Find how many clusters k are required to maintain distance
    Note: Nodes may have identical bitstrings. However, with the Union_Find Data Structure
    and algorithm that prioritizes 0 distance nodes, we can assume they have been 
    merged upon initialization.

    Parameters
    ----------
    nodes : Dictionary of str(bits):bytearray(bits)
    dist : Int
        DESCRIPTION. The default is 2.

    Returns
    -------
    k = number of clusters

    '''
    UF = union_find.UF(len(nodes))
    #Lookup Nodes by bitstring
    KeyDex = {}
    for ID, bstring in enumerate(nodes):
        KeyDex[bstring] = ID #bitstring: node ID
    for space in range(1, dist + 1): #Spaces from 1 to dist
        for bstring, bits in nodes.items():
            try:
                first = KeyDex[bstring]
            except:
                continue
            print("Dist: ", space, "Node: ",first)
            valids = HammingLim(bits, space)
            for valid in valids:
                vstring = ''.join([str(i) for i in valid])
                #print(vstring)
                if vstring in KeyDex:
                    second = KeyDex.pop(vstring)
                    UF.union(first, second)
    return UF.count()

#No need to actually consider diff nodes with 0 distance. They are effectively
#The same node.

#%% HammingCluster using NodesID, unfinished
def HammingCluster(nodes, dist = 2):
    '''
    Find how many clusters k are required to maintain distance
    Note: Nodes may have identical bitstrings. However, with the Union_Find Data Structure
    and algorithm that prioritizes 0 distance nodes, we can assume they have been 
    merged upon initialization.

    Parameters
    ----------
    nodes : Dictionary of str(bits):bytearray(bits)
    dist : Int
        DESCRIPTION. The default is 2.

    Returns
    -------
    k = number of clusters

    '''
    UF = union_find.UF(len(nodes))
    #Lookup Nodes by bitstring
    for space in range(1, dist + 1): #Spaces from 1 to dist
        for bstring in list(nodes.keys()):
            if bstring in nodes.keys():
                first = nodes[bstring][1]
            else:
                continue
            print("Dist: ", space, "Node: ",first)
            valids = HammingLim(nodes[bstring][0], space)
            for valid in valids:
                vstring = ''.join([str(i) for i in valid])
                #print(vstring)
                if vstring in nodes:
                    second = nodes.pop(vstring)[1]
                    UF.union(first, second)
    return UF.count()

#%% Time Testing
import time
from statistics import mean
tlist = []

for i in range(50):
    t1 = time.time()

    t2 = time.time()
    tlist.append(t2 - t1)

print(mean(tlist))

#%% Single Timer

t1 = time.time()
Result = HammingCluster(Nodes)
t2 = time.time() 

print(t2 - t1)
Time = 280.64604926109314 #Nodes without ID
Time = t2 - t1

#%% Single Timer for ID
t1 = time.time()
Result = HammingCluster(NodesID)
t2 = time.time() 

TimeID = t2 - t1