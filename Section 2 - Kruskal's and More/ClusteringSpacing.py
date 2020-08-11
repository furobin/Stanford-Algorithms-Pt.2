#%%
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#%%
from collections import namedtuple
from python_algorithms.basic import union_find

'''
UF: 
    find(self,p): finds set identifier of item p
    count(self): returns number of items, basically number of clusters
    connected(self, p q): checks if p and q in same cluster
    union(self, p, q): combines sets containing p and q
'''

#%%
Edge = namedtuple('Edge', ('vert1', 'vert2', 'dist'))

path = 'clustering1.txt'

Edges = []

with open(path, 'r') as f:
    n = int(f.readline())
    for line in f.readlines():
        V1, V2, dist = [int(x) for x in line.split(' ')]
        Edges.append(Edge(V1, V2, dist))

#Answer: 106

#%%
k = 4 #target number of clusters

def MaxSpacing (Edges,n, k):
    SEdges = sorted(Edges, key = lambda x: x.dist)
    UF = union_find.UF(n)
    while UF.count() >= k:
        edge = SEdges.pop(0)
        V1, V2 = edge.vert1 - 1, edge.vert2 - 1 #Fixing vert to match UF
        if not UF.connected(V1, V2) and UF.count() > k:
            print("Merging: ", V1, " ,", V2)
            UF.union(V1, V2)
        elif not UF.connected(V1, V2) and UF.count() == k:
            break
    return SEdges[0].dist

#%%
MaxSpacing(Edges, n, k)
    