# use a stack to reverse a string

string1 = "hello"
list1 = []

for char in string1:
    list1.append(char)

reverse = ""
while list1:
    reverse += list1.pop()

print(reverse)


