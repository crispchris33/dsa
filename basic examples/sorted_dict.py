#insertion

from sortedcontainers import SortedDict

sorted_dict = SortedDict()

sorted_dict['C'] = 90

sorted_dict['B'] = 80

sorted_dict['A'] = 70

print(sorted_dict)  # SortedDict({'A': 70, 'B': 80, 'C': 90})


#access

sorted_dict = SortedDict({'a': 1})

print(sorted_dict['a']) # 1


#delete

sorted_dict = SortedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

# removes & return the last key-value pair in sorted order
sorted_dict.popitem() # ('d', 1)

# removes & return the first key-value pair in sorted order
sorted_dict.popitem(0) # ('a', 1) 

# remove & return the value associated with the key
sorted_dict.pop('b') # 2

del sorted_dict['c'] # {}


#lookup

sorted_dict = SortedDict({'a': 1})

does_a_exist = 'a' in sorted_dict # True
does_b_exist = 'b' in sorted_dict # False


#iterating
sorted_dict = SortedDict({'a': 1, 'b': 2, 'c': 3})

for key, value in sorted_dict.items():
    print(key, value)

