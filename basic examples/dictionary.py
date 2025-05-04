#Insert
my_dict = {}

my_dict['a'] = 1 # {'a': 1}

#Access
my_dict = {'a': 1}

print(my_dict['a']) # 1

#Delete
my_dict = {'a': 1, 'b': 2}

del my_dict['a'] # {}

my_dict.pop('b') # {}

my_dict.pop('c') # KeyError: 'c'

my_dict.pop('c', 'default') # No error, returns 'default'

