#String Functions
#Ends with= it gives boolean value true if the string ends with the value we passed thru this function.

str= " I am studying python"
print( str.endswith("on") )
print( str.endswith("ng") )

#Capitalize= it capitalize the first letter of string.

str1 = "sukhchain singh"
print (str1.capitalize())

#Replace= it replace the old value to new value

str2= " I want to be an AI generalist"
print (str2.replace('a', 'u')) #will replace all a's in the string to u's.
#or
print( str2.replace("generalist", "engineer"))

#find= it returns first index of 1st occurrer.

print (str2.find("o")) #it will find the first occurrence of 'o' in the string

#count= it will count the occurence of passed letter or word in string.

print(str2.count("an"))

#if we want to explore more functions we can type str. to check all the available functions that will appear in drop down box.