import numpy as np
import itertools
G = np.loadtxt("regular.txt", int)

#Let's write a function that finds the sum of all the entries of a row.

def totalRow (x):
    total = 0
    for i in range (0, len (G)):
        total = total + G [int(x)] [int(i)]
    return total

def vertexSet ():
    vertexSet = set ()
    for x in range (0, len (G)):
        vertexSet.add (x)
    return vertexSet

#Let us now find the degree sequence.
#We will use an array.

def degreeSeq ():
    degreeSeq = []
    for i in range (0, len (G)):
        degreeSeq.append (totalRow (i))
    degreeSeq.sort (reverse = True)
    return degreeSeq


print (G)
print ("The vertexSet is ", vertexSet ())
print ("The degree sequence is ", degreeSeq ())
print (len (degreeSeq ()))
print (len (G))

#Okay, now I want to create a function that itteratively takes the "derivative"
#of a graph, G, and returns the "residue" i.e. the number of 0's left in the
#degree sequence after doing the derivative until are zeroes.


#A practice/problem solving function:
def calcResidue ():
    degseq = degreeSeq ()
    isDone = False

    while isDone == False:
        temp = degseq [0]
        zcount = 0
        isZero = False

        #Subtract 1 from the next "highest degree" number of entries
        for i in range (1, temp + 1):
            degseq [i] = degseq [i] - 1

        #Now remove the highest degree. 
        degseq.remove (temp)

        #Now sort the array
        degseq.sort (reverse = True)

        #This checks to see if you have all zeroes in the deree sequence:
        for i in range (0, len (degseq)):
            if degseq [i] == 0:
                zcount = zcount + 1
        
        #If you do, then exit the while loop
        if zcount == len (degseq):
            isDone = True
            
    return len(degseq)


print ("The residue of G is", calcResidue ())













#A practice/problem solving function:
def calcResidue1 ():
    degseq = degreeSeq ()
    isDone = False

    for i in range (0, 20):
        temp = degseq [0]
        zcount = 0
        isZero = False
        
        for i in range (1, temp + 1):
            degseq [i] = degseq [i] - 1

        print (degseq)
        degseq.remove (temp)
        print (degseq)
        degseq.sort (reverse = True)
        print ("Sorted is: ", degseq)


        #I need to make sure that I don't remove 0's when I don't want to.
        #Actually, I don't think I want to remove 0's. 
            
        #This checks to see if you have all zeroes in the deree sequence:
        for i in range (0, len (degseq)):
            if degseq [i] == 0:
                zcount = zcount + 1
        if zcount == len (degseq):
            isDone = True

        print (isDone)

    









    
    
