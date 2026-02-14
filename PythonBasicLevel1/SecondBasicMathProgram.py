a= 5
b= 29
sum = a+b
diff= a-b
multi= a*b
divide=b/a
modular =b%a #remainder
power = b**a #a to the power of b
print(sum, diff) #differentiate it with commas
"""
if you want to comment more than pne line either you can use this six commas method 
or you can select all the lines and then press ctrl + / """
print(multi, divide)

"""
arithmetic operators = (+, -, *, /, %, ** )
Relational/ comparison operators = ( ==, !=, >, <, >=, <= )
Assignment operators = ( =, +=, -=, *=, /=, %=, **= )
Logical operators = ( not, and, or )

"""
print(modular, power) # our arithmetic operators are fully used here

#Relational/ Comparison operators
a= 50
b= 20
c= 50
print(a==b) # this operator will tell if the value is true or false, 
            # as a is not equal to b the answer will be false
print(a!=b) #this operator will be true if a is not equal to b.
print(a>b) #this operator will be true as a is greater than b
print(a<b) #this operator will be false as a is not smaller than b
print(a>=c) # this will be true as c is equal to a.
print (a<=b) # this will be false as b is not greater than or equal to a

""" our Relational/ comparison operators are complete"""

#Assignment operators

''' we will use the assigned values that we assigned in the starting of this program and 
add, subtract, divide, multiply, find remainder, or the power of 10 with those values only)'''
num= 10 # ( = operator assigns value 10 to num )
sum +=10 # ( += operator means sum= sum + 10 )
diff -=10 # ( -= operator means diff= diff - 10 )
multi *=10 #(*= operator means multi = multi*10 )
divide /= 10 #similar as above
modular %=10 #similar as above
power ** 10 #similar as above

print (num, sum, diff, multi, divide, modular, power)

'''our assignment operators are done'''

#logical operators( these work on boolean values)

print (not False) # it will print true as not always prints opposite value
x= 30
y= 20
print( not(x>y)) # (x is greater than y but because we placed not in front so answer will be false.)

a1= True
b1= False 
print (a1 and b1) # (the answer will be false as for and operator to be true both a1 and b1 needs to be true)
print (a1 or b1) # ( the answer will be true as for or operator to be true only one statement needs to be true)
print ((x>y) or (x<y) ) # ( it will be true to as we applied or operator )

