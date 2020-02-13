import numpy as np
import itertools
G = np.loadtxt ("weightedgraph.txt", int)
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

print ("The weight of edge '1'", (G [1]))


#print (EdgeList [1])
#print (G [1])

def findMin0 (myarray):
    minWeight = weight (myarray [0])
    for i in range (0, len(myarray)):
        if (weight (myarray [i]) < minWeight):
            minWeight = weight (myarray [i])
    return minWeight

def findMin1 (myarray):
    minWeight = 0
    for i in range (0, len(myarray)):
        if (weight (myarray [i]) < weight (myarray [minWeight])):
            minWeight = i
    return minWeight

def findMin (edgeArray):
    minWeight = 0
    myarray = []
    for x in range (0, len (edgeArray)):
        myarray.append (G [edgeArray [x]])
    for i in range (0, len(myarray)):
        if (weight (myarray [i]) < weight (myarray [minWeight])):
            minWeight = i
    return edgeArray [minWeight]

            
def vertexSet ():
    mySet = set ()
    for i in range (0, len (G)):
        if G [i] [0] not in mySet:
            mySet.add (G [i] [0])
        if G [i] [1] not in mySet:
            mySet.add (G [i] [1])
    return mySet



#Let's create a funciton that finds the edge set of a vertex. We'll return an
#array

def edgeSet (v):
    myarray = []
    for i in range (0, len (G)):
        if G [i] [0] == v or G [i] [1] == v:
            myarray.append (i)
    return myarray

print ("The edge set of verex 1 is ", edgeSet (1))


#Let's create a function that, given a vertex determines the least cost edge.

def findMinCost (v):
    return (findMin (edgeSet (v)))

print ("The min cost edge for vertex 2 is", findMinCost (2), " i.e. ",
       G [findMinCost (2)])

def Prims (v):
    comparray = []
    treearray = []
    mySet = {v}
    while mySet != vertexSet ():
        for i in edgeSet (v):
            if i not in treearray: 
                comparray.append (i)
        print ("comp array is ", comparray)
        print ("min edge is", findMin (comparray))
        #You need something here to make sure you don't create a cycle..
        treearray.append (findMin (comparray))

        print ("tree is ", treearray)
        for i in range (0, 2):
            if G [findMin (comparray)] [i] != v:
                mySet.add (G [findMin (comparray)] [i])
                v = G [findMin (comparray)] [i]
        comparray.remove (findMin (comparray))
        print ("mySet  is now", mySet)
        print ("comp is now ", comparray) 
        print ("v is now", v)


def Prims1 (v):
    comparray = []
    treearray = []
    mySet = {v}
    
    while mySet != vertexSet ():
        countSet = set ()
        for i in edgeSet (v):
            if i not in treearray and (G [i] [0] not in mySet or G [i] [1] not
            in mySet): 
                comparray.append (i)
        print ("comp array is ", comparray)
        print ("min edge is", findMin (comparray))
        #You need something here to make sure you don't create a cycle..
        
        treearray.append (findMin (comparray))

        print ("tree is ", treearray)
        tempv = v
        for i in range (0, 2):
            if G [findMin (comparray)] [i] != tempv:
                print ("problem is ", G [findMin (comparray)] [i])
                mySet.add (G [findMin (comparray)] [i])
                v = G [findMin (comparray)] [i]
        comparray.remove (findMin (comparray))
        print ("comp is now" ,comparray)
        print (len(comparray))
        for i in range (0, len (comparray)):
            print (i)
            if G [comparray [i]][0] in mySet and G [comparray [i]][1] in mySet:
                print ("hello")
                countSet.add (comparray [i])
        for i in countSet:
            comparray.remove (i)
        print ("mySet is now", mySet)
        print ("comp is now ", comparray) 
        print ("v is now", v)
    print ("Done")
    return (treearray)



myarray = [1, 1, 2, 3]
print (0 in myarray)
print ("Tree is ........................ ", Prims1 (3))
print ("In other words: ")
for i in range (0, len(Prims1 (3))):
    print (G [i])

        
        

