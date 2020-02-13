#This program finds the greates common divisor of two numbers that the user
#enters using the Eucledian Algorithm.
#
#Author: Nick Montana
#
#Date: 3/21/17

cont = 'Y'
while (cont == 'Y'):
    print ("Enter two numbers")
    x = int (input("Number one: "))
    y = int (input("Number two: "))

    if (x > y):
        while (x != y):
            c = x - y
            if (c > y):
                x = c
            elif (y > c):
                x = y
                y = c
            else:
                x = c
        print ("GCD is: ", c)
    
    elif (y > x):
        while (x != y):
            c = y - x
            if (c > x):
                y = c
            elif (x > c):
                y = x
                x = c
            else:
                y = c
        print ("GCD is: ", c)

    else:
        print ("GCD is: ", x)
        
    print ()
    cont = input ("Would you like to continue? (Y or N) ")
    print ()

print ("Program Terminated")

        
