#1 - take a sum of number's digits

def sum_digits(n):
    if n < 10:
        return n
    
    return (n % 10) + sum_digits(n // 10)

#2 - reverse a string using recursion

def reverse_string(s):
    if len(s) <= 1:
        return s
    
    return s[-1] + reverse_string(s[:-1])


#2 - b - rverse a string

def reverse(s):
    if len(s) <= 1:
        return s
    
    return reverse(s[1:]) + s[0]

#3 - tower hanoi



print(sum_digits(123))
print(sum_digits(99773344))
print(sum_digits(555))
print("-" * 30)

print(reverse_string("hello"))
print(reverse_string("abcdefghijklmnopqrstuvwxyz"))
print(reverse_string("123"))
print(reverse_string("987"))
print(reverse_string("1234567890"))
print("-" * 30)
