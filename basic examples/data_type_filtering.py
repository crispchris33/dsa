'''

to remove one data type

isinstance(object, classinfo)

'''

#Check if a variable is a string:

x = "hello"
print(isinstance(x, str))  # True

#Check if a variable is an int:

x = 5
print(isinstance(x, int))  # True


#Check if variable is a string or an int

x = "hello"
print(isinstance(x, (str, int)))  # True



#remove char from a string
    # str.replace(target, replace_with)
    # s.replace("!", "")

#return a list of distinct elements(removing duplicates)

#   return sorted(set(seq))