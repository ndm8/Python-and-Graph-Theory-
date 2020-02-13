import numpy as np
import itertools
G = np.loadtxt ("weightedgraph.txt", int)
print (G)

def weight (e):
    return e [2]



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

def sortEdges ():
    sortedarray = []
    edgearray = []
    for i in range (0, len (G)):
        edgearray.append (i)
    for i in range (0, len (G)):
        x = findMin (edgearray)
        sortedarray.append (G [x])
        edgearray.remove (x)
    return sortedarray


def simpleSort1 ():
    sortedarray = []
    edgearray = []
    for i in range (0, len (G)):
        edgearray.append (i)
    for i in range (0, len (G)):
        x = findMin (edgearray)
        sortedarray.append (x)
        edgearray.remove (x)
    return sortedarray

def simpleSort ():
    myarray = []
    for i in range (0, len (G)):
        print ("check " , i)
        for j in range (0, len (sortEdges ())):
            print ("j is", j)
            if G [i].all() == sortEdges () [j].all():
                myarray.append (j)
            print (myarray)
    return myarray
                        


#We need to write a function that takes in an array of edges and determines
#if that collection is a cycle

def isCycle1 (edgearray0):
    edgearray = []
    for i in range (0, len (edgearray0)):
        edgearray.append (edgearray0 [i])
    if edgearray == []:
        return False
    V = G [edgearray [0]] [0]
    mover = G [edgearray [0]] [1]
    myedge = edgearray [0]
    nextv = -1
    already = {edgearray [0]}
    isCycle = False
    edgeSet = set ()
    for i in edgearray:
        edgeSet.add (i)
    for i in range (0, len (edgearray)): #I think I need a better while loop here 
        print ("i is ", i)

        #First, I need to find the edge that contains my mover:
        for i in edgearray:
            #This first if statement finds the edge which contains the mover
            #which is not already myedge and creates nextv. 
            if i != myedge and (G [i] [0] == mover or G [i] [1] == mover):
                if (G [i] [0] == mover) and isCycle == False:
                    nextv = G [i] [1]
                    already.add (i)
                    edgearray.remove (i)
                    edgeSet.remove (i)
                    print ("nextv is ", nextv)
                elif (G [i] [1] == mover):
                    nextv = G [i] [0]
                    already.add (i)
                    edgearray.remove (i)
                    edgeSet.remove (i)
                    print ("nextv is ", nextv)
            print ("already is", already)

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
                            already.add (i)
                            myedge = i
                            print ("mover is ", mover)
                        elif (G [i] [1] == nextv):
                            mover = G [i] [0]
                            already.add (i)
                            myedge = i
                            print ("mover is ", mover)
                    if mover == V:
                        isCycle = True
                        return isCycle
    return isCycle
                        


#We need to write a function that takes in an array of edges and determines
#if that collection is a cycle

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
        already = {i}
        isCycle = False
        edgeSet = set ()
        for i in edgearray:
            edgeSet.add (i)
        for i in range (0, len (edgearray)): #I think I need a better while loop here 
            print ("i is ", i)

            #First, I need to find the edge that contains my mover:
            for i in edgearray:
                #This first if statement finds the edge which contains the mover
                #which is not already myedge and creates nextv. 
                if i != myedge and (G [i] [0] == mover or G [i] [1] == mover):
                    if (G [i] [0] == mover):
                        nextv = G [i] [1]
                        already.add (i)
                        print ("nextv is ", nextv)
                    elif (G [i] [1] == mover):
                        nextv = G [i] [0]
                        already.add (i)
                        print ("nextv is ", nextv)
                print ("already is", already)

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
                                already.add (i)
                                myedge = i
                                print ("mover is ", mover)
                            elif (G [i] [1] == nextv):
                                mover = G [i] [0]
                                already.add (i)
                                myedge = i
                                print ("mover is ", mover)
                        if mover == V:
                            isCycle = True
                            return isCycle
    return isCycle                       
            
print (isCycle([0, 1, 2, 3, 4, 5]))





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



def isCycle2 (edgearray0):
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
        already = {i}
        isCycle = False
        edgeSet = set ()
        for i in edgearray:
            edgeSet.add (i)
        for i in range (0, len (edgearray)): #I think I need a better while loop here 
            

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
                                already.add (i)
                                myedge = i
                            
                            elif (G [i] [1] == nextv):
                                mover = G [i] [0]
                                already.add (i)
                                myedge = i
                            
                        if mover == V:
                            isCycle = True
                            return isCycle
    return isCycle












def Kruskal ():
    mySet = set ()
    treearray = []
    edgearray = simpleSort1 ()
    temparray = []
    while mySet != vertexSet ():
        for i in range (0, len (edgearray)):
            myedge = edgearray [i]
            print ("the edge is", edgearray [i])
            temparray.append (myedge)
            print ("temparray is ", temparray)
            if isCycle2 (temparray) == False: #cycle problem:
                myedge = edgearray [i]
                treearray.append (myedge)
                print ("treearray is now :  ", treearray)
                for i in range (0, 2):
                    mySet.add (G [myedge] [i])
                print ("mySet is now", mySet)
            else:
                print ("OH NO, ", temparray, "creates a cycle")
                print ("Now I need to remove, ", myedge, "from temparray")
                temparray.remove (myedge)
                print ("temparray is nooooowwwww: ", temparray)
    print ("The TREE is, ", treearray)


Kruskal ()
print (simpleSort1 ())

cyclearray = []
EdgeNumbers = set ()
for i in range (0, len (G)):
    EdgeNumbers.add (i)
for i in range (0, len (G)):
    for s in set(itertools.combinations (EdgeNumbers,i)):
        t = []
        for i in s:
            t.append (i)
        if isCycle2 (t):
            cyclearray.append (t)

print (cyclearray)


