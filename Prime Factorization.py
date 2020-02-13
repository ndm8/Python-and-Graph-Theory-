#This program finds the prime factorization of a number that the user enters.
#
#Author: Nick Montana
#
#Date: 3/21/17

cont = 'Y'
while (cont == 'Y'):
    x = int(input ("Enter a number: "))

    print ()
    print ("Prime Factorization is:")

    while (x%2 == 0):
        x = x / 2
        print (2)

    i = 3
    while (i <= x):
        while (x%i == 0):
            x = x / i
            print (i)
        i = i +2

    print ()
    cont = input ("Would you like to continue? (Y or N) ")
    print ()
    
        
        
