# for loop_variable in iterable:

# range works like this:
# range(start, stop, step)

# for i in range(1, 6):
#   print(i)

1. Triangle of Numbers
Write a program that prints the following pattern:

1
12
123
1234
12345

nums = 15
current_num = 1
rows = 5

for i in range(1, rows + 1):
    row = []

    for j in range(i):
        row.append(str(current_num))
        current_num += 1
    print(" ".join(row))



2. Reverse Triangle of Stars
Write a program to print this:

*****
****
***
**
*



num = 5
# range(start, stop, step)
for i in range(num, 0, -1):
    print('*' * i)


3. Floyd’s Triangle
Print the following pattern (numbers increase row by row):
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15


num = 15
num_str = ""
rows = 5
for i in range(1, num + 1):
        num_str += str(i) + " "
        print(num_str)


4. Square of Stars
Write a program to print a square of stars with n rows and columns:

*****
*****
*****
*****
*****


n = 5
star_str = ""
for i in range(1, n + 1):
    print('*' * n)


5. Multiplication Table
Write a program to print the multiplication table of a given number n. For example, if n = 5:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50


n = 5
value1 = ""
for i in range(1, 11):
   print(f"{n} X {i} = {n * i}")



6. Sum of First N Numbers
Write a program to calculate the sum of the first n natural numbers. For example, if n = 5, the sum is:

1 + 2 + 3 + 4 + 5 = 15


n = 5
sum = 0
result = ""

for i in range(1, n + 1):
    sum += i
    if i == n:
        result += f"{i}"
    else:
        result += f"{i} + "

result += f" = {sum}"
print(result)


7. Right-Aligned Triangle
Write a program to print a right-aligned triangle pattern:

    *
   **
  ***
 ****
*****

n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)




8. Diamond with Spaces
Write a program to print a diamond pattern with spaces:
   
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *


n = 9
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)


9. List Squares
Write a program that takes a list of numbers and prints the square of each number in the list. For example, given:

numbers = [1, 2, 3, 4, 5]

1
4
9
16
25

nums = [1, 2, 3, 4, 5]

for i in range(len(nums)):
    print(str(nums[i] * nums[i]))


10. Reverse a String
Write a program to reverse a string using a for loop. For example: Input: "hello" Output: "olleh"
   
string = "hello"
new = ""
for i in range(len(string) -1, -1, -1):
    new += string[i]
print(new)