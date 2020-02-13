#An attempt at the Eucledian Algorithm

print ("Please enter two numbers")
x = int (input("Number one: "))
y = int (input("Number two: "))
print (x - y)
print (x%y)
if ( x > y):
    print ("first is bigger")
    while (x > y):
        x = x - y
        print (x)
    while ( y > x):
        y = y - x
        print (y)
    while (x > y):
        x = x - y
        print (x)
    if ( x == y):
        print ("Done!")
        print (x)
else:
  print ("second is bigger")

