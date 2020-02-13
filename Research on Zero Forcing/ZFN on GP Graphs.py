#Zero Forcing Number on Generalized Petersen Graphs

#Nicholas Montana

import itertools

#First, I need to create a funtion that creates a 2D array that is the adjacency
#matrix of a Generalized Petersen Graph.

#First, let's define circulation
def circ (myarray):
    circarray = []
    circarray.append (myarray)

    #I need a previous array.
    prevarray = myarray
    
    for i in range (1, len(myarray)):
        temparray = []
        temparray.append (prevarray [len (prevarray) - 1])
        for i in range (1, len(myarray)):
            temparray.append (prevarray [i - 1])
        prevarray = temparray
        circarray.append (temparray)
    return circarray

#Let's create an Identity Matrix for the Adjancy Matrix:
def idenMat (n):
    idenarray = []
    
    for i in range (0, n):
        temparray = []
        for s in range (0, n):
            if (s == i):
                temparray.append (1)
            else:
                temparray.append (0)
        idenarray.append (temparray)
    return idenarray 


#Enter the parameters:
print ("Enter the parameters for a Generalized Petersen Graph defined by")
print ("GP (n, k): ")
n = int (input ("n: "))
k = int (input ("k: "))

#Let's create what to take the circulation of:
#Outer
def outer ():
    myarray = []
    for i in range (0, n):
        if i == 1:
            myarray.append (1)
        elif i == n - 1:
            myarray.append (1)
        else:
            myarray.append (0)
    return myarray

#Inner
def inner ():
    myarray = []
    for i in range (0, n):
        if i == k:
            myarray.append (1)
        elif i == n - 1 - (k - 1):
            myarray.append (1)
        else:
            myarray.append (0)
    return myarray

#This function creates the adjacency matrix:
def adjMat ():
    gparray = []
    Outer = circ (outer ())
    Inner = circ (inner ())
    for x in range (0, n):
        temparray = []
        for i in range (0, n):
            temparray.append (Outer [x] [i])

        for i in range (0, n):
            temparray.append (idenMat (n) [x] [i])
        gparray.append (temparray)

    for x in range (0, n):
        temparray = []
        for i in range (0, n):
            temparray.append (idenMat (n) [x] [i])

        for i in range (0, n):
            temparray.append (Inner [x] [i])
        
        gparray.append (temparray)
    return gparray

G = adjMat ()


def vertexSet ():
    vertexSet = set ()
    for x in range (0, len (G)):
        vertexSet.add (x)
    return vertexSet

#Let's form a neigbor set funciton.
#This function returns the neighbors of v as a set.

def N (v, G):
    neighbors = set ()
    for i in range (0, len (G)):
        if (G [v] [i] == 1):
            neighbors.add (i)
    return neighbors

print ("The Adjacency Matrix of GP(",n,",",k,") is: ")
for s in range (0, 2*n):
    print (G [s])

#Now let's do the Zero Forcing Number:

def isForce (Set):
    isForce = False
    force = True
    mySet = set ()
    size = len (Set)
    while Set != vertexSet () and force:
        for i in Set:
            counter = 0
            tempSet = set ()
            for x in N (i, G):
                if x in Set:
                    counter = counter + 1
                else:
                    tempSet.add (x)
            if counter == len (N (i,G)) - 1:
                mySet = set.union (mySet, tempSet)
        Set = set.union (Set, mySet)
        if len(Set) == size:
            force = False
        size = len (Set)
    if (Set == vertexSet ()):
        isForce = True
    return isForce

#Cut the graph in half to save on runtime
def halfVSet ():
    x = int ((n / 2) + 1)
    mySet = set ()
    for i in range (0, x):
        mySet.add (i)
    for j in range (n, n + x):
        mySet.add (j)
    
    return mySet


#Finds min ZFS
def findZFS ():
    for i in range (0, len (G)):
        for s in set (itertools.combinations (halfVSet (), i)):
            print ("Testing ...................", set (s))
            if (isForce (set (s))):
                return s

ZFS = findZFS ()
ZFN = len (findZFS ())
print ("The smallest Zero Forcing set is ", ZFS)
print ("The Zero Forcing Number is ", ZFN)


#Note: I am now using halfVSet () to cut computation time in half:
#GP Graphs have a certain bi-symmetry that we can take adantage of. 
#print ("The vertex set is ... ", vertexSet ())
#print (halfVSet ())



