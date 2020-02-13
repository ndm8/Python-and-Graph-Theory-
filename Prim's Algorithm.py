import numpy as np
import itertools
G = np.loadtxt ("weightedgraph.txt", int)
#print ("The edge list of G is: ", EdgeList)
#for i in range (0,len (G)):
 #   print(EdgeList [i])

V = {0,1,2,3,4,5,6}
for i in range (0, len (G)):
    for s in set (itertools.combinations (V,i)):
        print (s)
    
def dedgeWeight (e):
    weight = e[2]
    return weight
#print ("The wieght of edge 1 is: ", edgeWeight (e))

#The following initializes Prims Algorithm for MST.
V = {0}
H = {}
#print ("The initial set of vertices for H is: ", V"

A = {1, 2, 6}
B = {1, 2, 3, 4}

def incidentEdges (V,H):
    edges = set ()
    for i in V:
        for j in range (0, len(EdgeList)):
            if j not in H and (i == EdgeList [j] [0] or i == EdgeList [j] [1]):
                print ("Edge", EdgeList [j])
                edges.add (j)
    return edges
PossibleEdges = incidentEdges (V,H)
for i in PossibleEdges:
    print (edgeWight(EdgeList [i]))

minEdge = incidentEdges (V,H)[1]

            
