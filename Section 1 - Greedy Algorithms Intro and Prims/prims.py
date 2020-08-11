#%%
import os
import copy
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#%% Real File
path = 'edges.txt'

graph = Graph.from_edges(path)

#Correct Answer: -361829, cost of MST
#%% Test File
path = 'testedges.txt'

graph = Graph.from_edges(path)
#%% Another Test File
path = 'test2.txt'

graph = Graph.from_edges(path)

#Correct: -21939
#%% Nother Test
path = 'test3.txt'

graph = Graph.from_edges(path)

#Correct -2434994
#%%
class Graph:
    def __init__(self):
        self.verts = {} #Vertex ID, Vertex Obj
        self.edges = {} #Vertices, Cost
        
    @classmethod
    def from_edges(cls, path): #edge has V1, V2, cost
        obj = cls()
        with open(path, 'r') as file:
            nodenum, edgenum = [int(x) for x in file.readline().split(' ')]
            for edge in file.readlines():
                V1, V2, cost = [int(x) for x in edge.split(' ')]
                obj.edges[(V1, V2)] = cost #Undirected graph so this is okay, will not have a V2,V1 ordering in file
                if V1 not in obj.verts:
                    obj.verts[V1] = Vert(V1, {V2: cost})
                else: # V1 in self.verts
                    obj.verts[V1].adj[V2] = cost
                if V2 not in obj.verts:
                    obj.verts[V2] = Vert(V2, {V1: cost})
                else: # V2 in self.verts
                    obj.verts[V2].adj[V1] = cost
        print("Loaded graph with ", nodenum, " nodes and ", edgenum, " edges.")
        return obj
    
#%% Fairly naive implementation
def Prims(Graph, Vert):
    Graph = copy.deepcopy(Graph)
    X = set()
    X.add(Vert.ID)#Stores vertices objects already seen
    T = set() #Edges added
    score = 0
    #for i in range(10):
    while len(X) != len(Graph.verts):
        look = {}
        for edge in Graph.edges:
            if (edge[0] in X) ^ (edge[1] in X):
                #print(edge[0], " in X")
                look[edge] = Graph.edges[edge]
        #print(sorted(look.items(), key = lambda x: x[1]))
        MinEdge = sorted(look.items(), key = lambda x: x[1]).pop(0)
        #print(MinEdge)
        V1 = MinEdge[0][0] #Assigning Vertex ID for easy use
        V2 = MinEdge[0][1] #ssigning Vertex ID for easy use
        T.add(MinEdge[0])
        score += Graph.edges.pop(MinEdge[0])
        #print(score)
        #print("Removed edge: ", MinEdge[0])
        for v in (V1, V2):
            X.add(v)
    return X, T, score
                



''' Deletes all edges with either V1 or V2 in it
for edge in list(Graph.edges): #looking at all remaining edges
    if V1 in edge or V2 in edge: #Remove edge containing added verts
        print("Removing Edge: ", edge)
        Graph.edges.pop(edge)
'''
#%% Vert Class with MinCost Prop
class Vert:
    '''
    Properties:
    
        ID: ID Number
        edges: IDs of adjacent nodes that are heads of this node
        
    '''
    
    def __init__(self, ID, adj = {}):
        self.ID = ID
        self.adj = adj #dict[adj node] = edge cost
        self.minHead = None
        self.minCost = float('inf')
          
    def __eq__(self, other):
        if isinstance(other, Vert):
            return self.ID == other.ID
        else:
            return self.ID == other
    
    def __hash__(self):
        return self.ID
    
    def __lt__(self, other):
        assert isinstance(other, Vert)
        return self.minCost < other.minCost
    
    def __le__(self, other):
        assert isinstance(other, Vert)
        return self.minCost <= other.minCost
    
    def __repr__(self):
        return (str((self.ID, self.minCost)))

#%%
class MinHeap:
    
    def __init__(self, data = []):
        self.data = data.copy()
    
    @classmethod
    def Heapify(cls, data = []):
        for root in range(len(data)//2-1, -1, -1):
            rootVal = data[root]
            child = root * 2 + 1
            while child < len(data):
                if child + 1 < len(data) and data[child] > data[child + 1]:
                    child +=1 #Finding minimum of 2 children
                if rootVal <= data[child]:
                    break
                data[child], data[(child-1)//2] = data[(child-1)//2], data[child]
                child = child * 2 + 1
        obj = cls(data)
        return obj
    
    def FindParent(self, index):
        assert index <= len(self.data) - 1, "Index out of range"
        parent = (index -1)//2
        return self.data[parent]
        
    def FindChild(self, index):
        child = index * 2 + 1
        if child + 1 <= len(self.data) - 1:
            return (self.data[child], self.data[child + 1])
        elif child == len(self.data) - 1:
            return self.data[child]
        #else:
            #print("No Child")
            
    def MinChild(self, index):
        Children = self.FindChild(index)
        if type(Children) == tuple:
            return min(Children)
        else:
            return Children
        
    def ExtractMin(self):
        if len(self.data) == 1:
            Min = self.data.pop()
        else:
            self.data[0], self.data[-1] = self.data[-1], self.data[0] #Swap positions of first and last
            Min = self.data.pop() #Returns and removes last element i.e. minimum
            num = self.data[0]
            index = 0 #Set current index of num to bubble down
            target = self.MinChild(index) #Minimum of children
            while self.FindChild(index) != None and num > target: #Bubbling down
                child = self.data.index(target, index * 2 + 1)  #Find index of minimum of children
                self.data[index], self.data[child] = self.data[child], self.data[index] #Swapping
                index = child       
                target = self.MinChild(index)            
        return Min
        
    def Insert(self, num):
        self.data.append(num)
        index = len(self.data) - 1
        while index > 0 and num < self.FindParent(index):
            parent = (index + 1)//2 - 1
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent
        
        
    def Remove(self, index):
        '''
        Removes item and heap index; maintains heap structure
        Parameters
        ----------
        index : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        if index == len(self.data) - 1:
            self.data.pop() 
        else:
            self.data[index], self.data[-1] = self.data[-1], self.data[index]
            self.data.pop()
            num = self.data[index]
            if self.MinChild(index) != None:
                target = self.MinChild(index)
            while self.FindChild(index) != None and num > target:
                target = self.MinChild(index)
                child = self.data.index(target, index * 2 + 1)  #Find index of minimum of children
                self.data[index], self.data[child] = self.data[child], self.data[index] #Swapping
                index = child       

#%% Heaps with vertices, not working properly so far
def HPrims(Graph, Source):
    Graph = copy.deepcopy(Graph)
    X = set()
    X.add(Source.ID)#Stores vertices IDs
    T = set() #Edges added
    score = 0
    def minCost(vert, new = None): #Internal count of minCost
        if new == None:
            adjs = [adj for adj in vert.adj.items() if adj[0] in X] #list of tuples, 
            if adjs:
                edge = min(adjs, key = lambda x: x[1])
                vert.minHead = edge[0] #Assigns minimum head
                vert.minCost = edge[1] #Assigns minimum cost
        elif new != None:
            if vert.minCost > vert.adj[new]: #Takes new ID
                vert.minCost = vert.adj[new]
                vert.minHead = new
    for adj in Source.adj:
        minCost(Graph.verts[adj])
    H = MinHeap().Heapify([Graph.verts[adj] for adj in Source.adj])
    for vert in Graph.verts:
        if vert not in H.data and vert != Source:
            minCost(Graph.verts[vert])
            H.data.append(Graph.verts[vert])    
    while H.data:
        new = H.ExtractMin() #Vertex Object
        #print("Added: ", new)
        #print(H.data)
        X.add(new.ID) #adding new Vertex to X
        T.add((new.ID, new.minHead)) #adding new Edge to T
        score += new.minCost #recording cost
        for adj in list(new.adj):
            #print("Looking at: ", adj)
            if adj in X:
                new.adj.pop(adj)
            else:
                #print("Removing and Inserting: ", adj)
                index = H.data.index(adj)
                H.Remove(index)
                minCost(Graph.verts[adj], new.ID)
                H.Insert(Graph.verts[adj])
    return X, H, T, score, Graph
            
            
            
    #Need to clear out adj elements from node as added to 
    
    '''
    while len(X) != len(Graph.verts)
        while len(X) != len(Graph.verts):
        look = {}
        for edge in Graph.edges:
            if (edge[0] in X) ^ (edge[1] in X):
                #print(edge[0], " in X")
                look[edge] = Graph.edges[edge]
        print(sorted(look.items(), key = lambda x: x[1]))
        MinEdge = sorted(look.items(), key = lambda x: x[1]).pop(0)
        #print(MinEdge)
        V1 = MinEdge[0][0] #Assigning Vertex ID for easy use
        V2 = MinEdge[0][1] #ssigning Vertex ID for easy use
        T.add(MinEdge[0])
        score += Graph.edges.pop(MinEdge[0])
        #print(score)
        #print("Removed edge: ", MinEdge[0])
        for v in (V1, V2):
            X.add(v)
    '''
    
#%%
import time

t1 = time.time()
HPrims(graph, graph.verts[1])
t2 = time.time()
print("Heap Elapsed: ", t2-t1)

t1 = time.time()
Prims(graph, graph.verts[1])
t2 = time.time()
print("Naive Elapsed: ", t2 - t1)

#%% 
import heapq
import timeit

print("Heapify Tests")
t1 = time.time()
test = MinHeap.Heapify(test1)
t2 = time.time()
print("Custom: ", t2 - t1)

t1 = time.time()
heapq.heapify(test1)
t2 = time.time()
print("Heapq: ", t2 - t1)

print("Extract Min Tests")
t1 = time.time()
test.ExtractMin()
t2 = time.time()
print("Custom: ",t2 - t1)

t1 = time.time()
heapq.heappop(test1)
t2 = time.time()
print("Heapq: ", t2 - t1)

print("Insert Tests")
t1 = time.time()
test.Insert(35)
t2 = time.time()
print("Custom: ", t2-t1)

t1 = time.time()
heapq.heappush(test1, 35)
t2 = time.time()
print("Heapq: ", t2 - t1)

'''
Basically, heapq is miles above whatever my shit is for heapify.
However, for Extract Min and Insert, we seem to be on par. Nice
'''
