import numpy as np
import itertools
G = np.loadtxt ("finalw.txt", int)
print (G)

def n (G):
    return len (G)

#Let's define an edge list, not sure what this is for?
EdgeList = []
for i in range (0, n (G)):
    EdgeList.append (G [i])

#Let's define an edge weight. This function takes in an edge and returns its
#weight.

def weight (e):
    return e [2]

#This function takes in an array of edges and returns the edge which has the
#minimum weight 
def findMin (edgeArray):
    minWeight = 0
    myarray = []
    for x in range (0, len (edgeArray)):
        myarray.append (G [edgeArray [x]])
    for i in range (0, len(myarray)):
        if (weight (myarray [i]) < weight (myarray [minWeight])):
            minWeight = i
    return edgeArray [minWeight]

#This function returns the vertex set of G            
def vertexSet ():
    mySet = set ()
    for i in range (0, len (G)):
        if G [i] [0] not in mySet:
            mySet.add (G [i] [0])
        if G [i] [1] not in mySet:
            mySet.add (G [i] [1])
    return mySet

#Let's create a funciton that finds the edges coming out of a vertex.
#We'll return an array

def edgeSet (v):
    myarray = []
    for i in range (0, len (G)):
        if G [i] [0] == v or G [i] [1] == v:
            myarray.append (i)
    return myarray

#Let's create a function that, given a vertex determines the least cost edge.
def findMinCost (v):
    return (findMin (edgeSet (v)))


#Here's Prim's Algorithm:
def Prims (v):
    comparray = []
    treearray = []
    mySet = {v}
    
    while mySet != vertexSet ():
        countSet = set ()
        for i in edgeSet (v):
            if i not in treearray and (G [i] [0] not in mySet or G [i] [1] not
            in mySet): 
                comparray.append (i)
        treearray.append (findMin (comparray))
        tempv = v
        for i in range (0, 2):
            if G [findMin (comparray)] [i] != tempv:
                mySet.add (G [findMin (comparray)] [i])
                v = G [findMin (comparray)] [i]
        comparray.remove (findMin (comparray))
        for i in range (0, len (comparray)):
            if G [comparray [i]][0] in mySet and G [comparray [i]][1] in mySet:
                countSet.add (comparray [i])
        for i in countSet:
            comparray.remove (i)
    return (treearray)

x = int (input ("Enter the vertex you wish to apply Prim's: "))
print ("The minimum spanning tree is", Prims (x))
print ("In other words, the edges: ")
for i in Prims (x):
    print (G [i])

        
        

