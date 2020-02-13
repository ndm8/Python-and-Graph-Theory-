import numpy as np
import itertools
G = np.loadtxt ("finalw.txt", int)
print (G)

#This function returns the weight of an edge. 
def weight (e):
    return e [2]

#This function returns the vertex set of G
def vertexSet ():
    mySet = set ()
    for i in range (0, len (G)):
        if G [i] [0] not in mySet:
            mySet.add (G [i] [0])
        if G [i] [1] not in mySet:
            mySet.add (G [i] [1])
    return mySet

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

#This function sorts the edges of G by inscreasing weight. 
def simpleSort ():
    sortedarray = []
    edgearray = []
    for i in range (0, len (G)):
        edgearray.append (i)
    for i in range (0, len (G)):
        x = findMin (edgearray)
        sortedarray.append (x)
        edgearray.remove (x)
    return sortedarray

#This function takes in an array of edges and determines whether or not those
#edges create a cycle or have a cycle in them. 
def isCycle (edgearray0):
    edgearray = []
    for i in range (0, len (edgearray0)):
        edgearray.append (edgearray0 [i])
    if edgearray == []:
        return False
    for i in edgearray:
        V = G [i] [0]
        mover = G [i] [1]
        myedge = i
        nextv = -1
        isCycle = False
        already = {i}
        for i in range (0, len (edgearray)): 
            #First, I need to find the edge that contains my mover:
            for i in edgearray:
                #This first if statement finds the edge which contains the mover
                #which is not already myedge and creates nextv. 
                if i != myedge and (G [i] [0] == mover or G [i] [1] == mover):
                    if (G [i] [0] == mover):
                        nextv = G [i] [1]
                        already.add (i)
                        
                    elif (G [i] [1] == mover):
                        nextv = G [i] [0]
                        already.add (i)
                        
                #Is it a cycle? If not, move on 
                if nextv == V:
                    isCycle = True
                    return isCycle
                    
                #Now I need to change myedge and the mover.
                else:
                    for i in edgearray:
                        if i not in already and (G [i] [0] == nextv or G [i] [1]
                                                 == nextv):
                            if (G [i] [0] == nextv):
                                mover = G [i] [1]
                                myedge = i
                            
                            elif (G [i] [1] == nextv):
                                mover = G [i] [0]
                                myedge = i
                                
                        #Is it a cycle now? If not move on    
                        if mover == V:
                            isCycle = True
                            return isCycle
    return isCycle

#Here's Kruskal's Algorithm:
def Kruskal ():
    mySet = set ()
    treearray = []
    edgearray = simpleSort ()
    temparray = []
    while mySet != vertexSet ():
        for i in range (0, len (edgearray)):
            myedge = edgearray [i]
            temparray.append (myedge)
            if isCycle (temparray) == False: #cycle problem:
                myedge = edgearray [i]
                treearray.append (myedge)
                for i in range (0, 2):
                    mySet.add (G [myedge] [i])
            else:
                temparray.remove (myedge)
                
    return treearray


print ("The minimum spanning tree is: ", Kruskal ())
print ("In other words, the edges: ")
for i in Kruskal ():
    print (G [i])

cyclearray = []
EdgeNumbers = set ()
for i in range (0, len (G)):
    EdgeNumbers.add (i)
for i in range (0, len (G)):
    for s in set(itertools.combinations (EdgeNumbers,i)):
        t = []
        for i in s:
            t.append (i)
        if isCycle (t):
            cyclearray.append (t)

print ("These are all the collections of edges which are cycles or",
       "contain a cycle:")
print (cyclearray)


