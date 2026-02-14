#Slicing= It is used to accessing parts of the string.It can be used using index(idx) of string
#It can be written as str[ starting_idx : ending_idx ] #ending idx is not included, for example if ending index is 4. 4th character will be excluded.

str = "Sukhchain Singh"
slicing= str[0 : 4]
print(slicing)
# if we want to write till the end of string there are 2 additional ways of write it.

print (str[ 0: len (str)])
print (str[0 :]) #you can miss the starting or ending of index to start from beginning or go till end.

#Slicing using negative index. its used to count string from backside of string. it starts from end and starts from -1

str2 = "Singh"
print (str[-3: -1])