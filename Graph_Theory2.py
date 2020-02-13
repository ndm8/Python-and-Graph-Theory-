import numpy as np
G = np.loadtxt("graph.txt", int)
def n (G):
    return len (G)
print (G)
#print (G[1][1])
#print (len (G))
print ("The number of vertices in G is ", n (G))


#let's write a function that finds the sum of all the entries of a row
#determined by the user.

#x = input ("Enter which row: ")
def totalRow (x):
    total = 0
    for i in range (0, n (G)):
        total = total + G [int(x)] [int(i)]
    return total

#print (totalRow (x))

sum = 0
for  i in range (0, n (G)):
    sum = sum + totalRow (i)

print ("The number of edges in G is ", int(sum / 2))

#Let's create the degree set.
VertexSet = set ()
for i in range (0, n (G)):
    VertexSet.add (totalRow (i))

print ("The degree set is ", VertexSet)

print ("The max degree is ", max (VertexSet))
print ("The min degree is ", min (VertexSet))

#Let us now find the degree sequence.
#We will use an array.

def degreeSeq ():
    degreeSeq = []
    for i in range (0, n (G)):
        degreeSeq.append (totalRow (i))
    degreeSeq.sort (reverse = True)
    return degreeSeq
    
print ("The degree sequence of G is: ", degreeSeq ())
    

#Let's form a neigbor set funciton.
#This function returns the neighbors of v as a set.

def N (v, G):
    neighbors = set ()
    for j in range (0, n (G)):
        if (G [v] [j] == 1):
            neighbors.add (j)
    return neighbors

print ()
print ("The neighbor set of 0 is: ", N (0, G))

#We now need to construct a function that finds the distance between any two
#vertices in a path, that is, finds the length of the shortest path between
#them.

#def d (u, v):
 #   counter = 0
  #  y = u
   # for x in N(y, G):
    #    while (!(v in N (y, G))):
     #       counter = counter + 1
      #      y = 
            
#def d (u, v):
 #   counter = 0
  #  if (v in N(u, G)):
   #     counter = 1
    #else:
     #   for i in range (0, n (G)):
      #      if (v in N(i, G)):
       #         x = i
        #while (set.intersection (N (u,G), N(x, G)) == set ()):
         #   counter = counter + 1
#    return counter

#Okay, this definition for distance works, but it can be faster
#def f (u, v):
 #   theSet = N (u, G)
  #  counter = 1
   # while (v not in theSet):
    #    counter = counter +1
     #   for x in theSet:
      #      theSet = set.union (theSet, N (x,G))
    #return counter

#Here is the best definition for distance that I have. It finds the length
#of the shortest path between two vertices u and v.
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

def eccentricity (v):
    return max (distanceSet(v))

        
print ("The distance between 0 and 6 is: ", d (0, 3))
print ("The distance set of 0 is: ", distanceSet (0))
print ("The distance set of 3 is: ", distanceSet (3))
print ("The eccentricity of 0 is: ", eccentricity (0))
print ("The eccentricity of 1 is: ", eccentricity (1))
print ("The eccentricity of 2 is: ", eccentricity (2))
print ("The eccentricity of 3 is: ", eccentricity (3))
#print ("The eccentricity of 4 is: ", eccentricity (4))
#print ("The eccentricity of 5 is: ", eccentricity (5))
#print ("The eccentricity of 6 is: ", eccentricity (6))
    
#Now let us form the eccentrincity set:
def eccSet ():
    eccSet = set ()
    for i in range (0, n (G)):
        eccSet.add (eccentricity (i))
    return eccSet
print ("The eccentricity set of G is: ", eccSet ())

#Now let's define radius and diameter:
def radius ():
    return min (eccSet ())

def diameter ():
    return max (eccSet ())

print ("The radius of G is: ", radius ())
print ("The diameter of G is: ", diameter ())

#Let's try to form the largest possible clique with 0:

def vertexSet ():
    vertexSet = set ()
    for x in range (0, n (G)):
        vertexSet.add (x)
    return vertexSet
        
#I think this works for small graphs, but I am not too sure about larger ones.
#Also, I am encountering some problems with it. Maybe I should draw it out.
def cliqueSet (v):
    clique = {v}
    theSet = N (v, G)
    noclique = True
    while (noclique):
        for x in theSet:
            for y in theSet:
                 if (y in set.union (N (x, G), {x}) and noclique):
                     clique.add (y)
                 else:
                    noclique = False
      #  for z in theSet:
       #             theSet = set.union (theSet, N (z,G))
        if (len(clique) == len(vertexSet ())):
            noclique = False
        noclique = False
        
    return clique

#def cliqueSet2 (v):
 #   clique = {v}
  #  theSet = N (v, G)
   # noclique = True
    #for x in theSet:
     #   for y in theSet:
      #       if (y in set.union (N (x, G), {x}) and noclique):
       #         clique = set.union (clique, theSet)
        #     else:
         #       noclique = False
  #  return clique

print ("The largest clique for 6: ", cliqueSet (6))
for i in range (0, n (G)):
    print ("The largest clique for ", i, " ", cliqueSet (i))

def cliqueNum ():
    cliqSizes = set ()
    for i in range (0, n (G)):
        cliqSizes.add (len (cliqueSet (i)))
    return max (cliqSizes)

print ("The clique number of G is : ", cliqueNum ())

#Now let's try to find the independence number.
#Not too sure if this works all the time...
def indSet ():
    indSet = vertexSet () #Assume it is the whole graph
    x = 0
    tempSet = vertexSet ()
    for x in indSet:
        if (x in indSet):
            indSet = set.difference (indSet, N (x, G))
    return indSet

print ("The largest independent set is: ", indSet ())
print ("The independence number is: ", len (indSet ()))

#Proper coloring: First, we will create an empty array. Then, we will create a
#set with the 0th verticy. This will be the set with the first coloring. We will
#add its neighbors to a second set, the second color. Then, we will attempt to
#color its neighbors (exculding the 0 in our first set) the same color as the
#first set. Rinse, wash, repeat. Keep track of which ones have been colored.

def colorArray ():
    my_array = []
    mySet = {0}
    my_array.append (mySet)
    colored = {0}
    for i in vertexSet ():
        if (i in colored):
            newSet = N (i, G)
            my_array.append (newSet)
            for x in N (i, G):
                colored.add (x)
        
        
        










