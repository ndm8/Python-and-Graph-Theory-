import numpy as np
import itertools
G = np.loadtxt("graph.txt", int)

def n (G):
    return len (G)

#Let's write a function that finds the sum of all the entries of a row.

def totalRow (x):
    total = 0
    for i in range (0, n (G)):
        total = total + G [int(x)] [int(i)]
    return total

def numEdges ():
    sum = 0
    for  i in range (0, n (G)):
        sum = sum + totalRow (i)
    return int(sum / 2)

#Let's create the degree set.
DegreeSet = set ()
for i in range (0, n (G)):
    DegreeSet.add (totalRow (i))

def vertexSet ():
    vertexSet = set ()
    for x in range (0, n (G)):
        vertexSet.add (x)
    return vertexSet

#Let us now find the degree sequence.
#We will use an array.

def degreeSeq ():
    degreeSeq = []
    for i in range (0, n (G)):
        degreeSeq.append (totalRow (i))
    degreeSeq.sort (reverse = True)
    return degreeSeq

#Let's form a neigbor set funciton.
#This function returns the neighbors of v as a set.

def N (v, G):
    neighbors = set ()
    for j in range (0, n (G)):
        if (G [v] [j] == 1):
            neighbors.add (j)
    return neighbors

#We now need to construct a function that finds the distance between any two
#vertices in a path, that is, finds the length of the shortest path between
#them.

def d (u, v):
    if (u == v):
        counter = 0
    else:
        theSet = N (u, G)
        counter = 1
        while (v not in theSet):
            counter = counter +1
            tempSet = theSet
            for x in theSet:
                theSet = set.union (theSet, N (x,G))
            theSet =  set.difference (theSet, tempSet)
    return counter

#Now let's contrust a function that finds the the "Distance Set", i.e.
#given a vertex v, it will collect the distances between v and all the
#other vertices in a graph.

def distanceSet (v):
    distanceSet = set ()
    for x in range (0, n (G)):
        distanceSet.add (d (v, x))
    return distanceSet

#Eccentricity:

def eccentricity (v):
    return max (distanceSet(v))

#Now let us form the eccentrincity set:

def eccSet ():
    eccSet = set ()
    for i in range (0, n (G)):
        eccSet.add (eccentricity (i))
    return eccSet

#Now let's define radius and diameter:

def radius ():
    return min (eccSet ())

def diameter ():
    return max (eccSet ())

#Driver/Main:

print (G)

print ()

print ("The number of vertices in G is ", n (G))

print ("The number of edges in G is ", numEdges ())

print ("The degree set is ", DegreeSet)

print ("The max degree is ", max (DegreeSet))

print ("The min degree is ", min (DegreeSet))
    
print ("The degree sequence of G is: ", degreeSeq ())

print ("The neighbor set of 0 is: ", N (0, G))

print ()

print ("The distance between 0 and 3 is: ", d (0, 3))
print ("The distance set of 0 is: ", distanceSet (0))
print ("The distance set of 3 is: ", distanceSet (3))
print ()
print ("The eccentricity of 0 is: ", eccentricity (0))
print ("The eccentricity of 1 is: ", eccentricity (1))
print ("The eccentricity of 2 is: ", eccentricity (2))
print ("The eccentricity of 3 is: ", eccentricity (3))

print ("The radius of G is: ", radius ())
print ("The diameter of G is: ", diameter ())

print ()



#I'm going to create some test functions:

def isIndSet (Set):
    isInd = True
    for x in Set:
        for y in Set:
            if y in N(x, G):
                isInd = False 
    return isInd

def isCliq (Set):
    isCliq = True
    for x in Set:
        for y in Set:
            if y not in N(x,G) and x != y:
                isCliq = False
    return isCliq

def isDom (Set):
    isDom = True
    NeighborSet = set ()
    for x in Set:
        NeighborSet = set.union (N(x,G), NeighborSet)

    for i in set.difference(vertexSet (), Set):
        if (i not in NeighborSet):
            isDom = False
    return isDom

def isTotalDom (Set):
    isTotalDom = True
    NeighborSet = set ()
    for i in Set:
        NeighborSet = set.union (N(i,G), NeighborSet)
    for i in vertexSet ():
        if i not in NeighborSet:
            isTotalDom = False
    return isTotalDom



print (isIndSet ({1, 3}))
print (isCliq ({0,3,2}))
print (isDom ({1,3}))
print (isTotalDom ({1,3}))

for i in range (0, len (G)):
        for s in set (itertools.combinations (vertexSet (),i)):
            print (s)

#Function findMaxInd finds the index of the largest independent set and prints
#the set
def findMaxInd ():
    indArray = []
    for i in range (0, len (G)):
        for s in set (itertools.combinations (vertexSet (),i)):
            if (isIndSet (s)):
                indArray.append (s)
    print (indArray)
    max = 0 
    for i in range (0, len (indArray)):
        if len (indArray [i]) > len (indArray [max]):
            max = i
    print ("The largest independent set is ", indArray [max])
    print ("The indepence number is ", len (indArray [max]))



#Finds largest clique
def findMaxCliq ():
    cliqArray = []
    for i in range (0, len (G)):
        for s in set (itertools.combinations (vertexSet (),i)):
            if (isCliq (s)):
                cliqArray.append (s)
    print (cliqArray)
    max = 0 
    for i in range (0, len (cliqArray)):
        if len (cliqArray [i]) > len (cliqArray [max]):
            max = i
    print ("The largest clique set is ", cliqArray [max])
    print ("The clique number is ", len (cliqArray [max]))



#How do I do a coloring? I can assume I can do it with 1 color, test, 2 colors?
#test...but the only problem is when testing 2 colors, where do I place those
#colors??? If I

#Finds largest clique
def findMinDom ():
    domArray = []
    for i in range (0, len (G)):
        for s in set (itertools.combinations (vertexSet (),i)):
            if (isDom (s)):
                domArray.append (s)
    print (domArray)
    min = 0 
    for i in range (0, len (domArray)):
        if len (domArray [i]) < len (domArray [min]):
            min = i
    print ("The smallest dominating set is ", domArray [min])
    print ("The domination number is ", len (domArray [min]))



#Finds largest clique
def findMinTotalDom ():
    TotaldomArray = []
    for i in range (0, len (G)):
        for s in set (itertools.combinations (vertexSet (),i)):
            if (isTotalDom (s)):
                TotaldomArray.append (s)
    min = 0 
    for i in range (0, len (TotaldomArray)):
        if len (TotaldomArray [i]) < len (TotaldomArray [min]):
            min = i
    print ("The smallest total dominating set is ", TotaldomArray [min])
    print ("The total domination number is ", len (TotaldomArray [min]))

findMinTotalDom ()

#This function and the next help to find the Chromatic number of G.

def findIndSet (Set):
    indSet = Set           #Assume it is the whole graph
    for x in indSet:
        if (x in indSet):
            indSet = set.difference (indSet, N (x, G))
    return indSet

print ("The largest ind. set for {1, 2, 4} is: ", findIndSet({1, 2, 4}))
print ("The largest ind. set for {2} is: ", findIndSet ({2}))

#This works very well I think for finding the Chromatic number of G:
def colorG ():
    mySet = vertexSet ()
    colored = set ()
    my_array = []
    while (colored != vertexSet ()):
        my_array.append (findIndSet(mySet))
        for i in findIndSet (mySet):
            colored.add (i)
        mySet = set.difference (mySet, findIndSet(mySet))
    return my_array

print ("The chromatic number of G is ", len(colorG ()), " with solution ",
       colorG ())


#Zero Forcing: start with a set. Does that set force the graph?

def isForce (Set):
    isForce = False
    mySet = set ()
    while Set != vertexSet () or force:
        for i in Set:
            print ("Check ", i)
            counter = 0
            tempSet = set ()
            for x in N (i, G):
                print (x)
                if x in Set:
                    print (x, " is in Set!")
                    counter = counter + 1
                    print (counter)
                    print (len (N(i,G)))
                else:
                    print (x, "can be forced?")
                    tempSet.add (x)
                    #I don't want to just add things that are
                    #neighbors but not in my Set. Only add if it can be
                    #be forced. But otherwise "x" will just be the last
                    #thing I checked. 
                if counter == len (N (i,G)) - 1:
                    force = True
                    print ("It forced! :)")
                    mySet = set.union (mySet, tempSet)
                    print (mySet)
                else:
                    force = False
                    print ("It didn't force :(")
        Set = set.union (Set, mySet)
        
        print ("My new ZFS is", Set)
        print ("Hello")
    if (Set == vertexSet ()):
        isForce = True
    return isForce
        

#Zero Forcing: start with a set. Does that set force the graph?
#Produces an infant loop 
def isForce1 (Set):
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


#Finds min ZFS
def findZFN ():
    ZFSArray = []
    for i in range (0, len (G)):
        for s in set (itertools.combinations (vertexSet (), i)):
            if (isForce1 (set (s))):
                ZFSArray.append (s)
    min = 0 
    for i in range (0, len (ZFSArray)):
        if len (ZFSArray [i]) < len (ZFSArray [min]):
            min = i
    print ("The smallest ZFS set is ", ZFSArray [min])
    print ("The ZFN is ", len (ZFSArray [min]))

findZFN ()
print (isForce1 ({1, 3}))



    




