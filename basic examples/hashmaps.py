#insert

my_dict = {}

my_dict['a'] = 1 # {'a': 1}

#access
my_dict = {'a': 1}

print(my_dict['a']) # 1

#delete
my_dict = {'a': 1, 'b': 2}

del my_dict['a'] # {}

my_dict.pop('b') # {}

my_dict.pop('c') # KeyError: 'c'

my_dict.pop('c', 'default') # No error, returns 'default'

#lookup
my_dict = {'a': 1}

does_a_exist = 'a' in my_dict # True
does_b_exist = 'b' in my_dict # False
