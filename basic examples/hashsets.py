#insert

my_set = set()

my_set.add('a') # {'a'}


#delete

my_set = {'a'}

my_set.remove('a') # {}
my_set.remove('a') # KeyError

my_set.add('b') # {'b'}
my_set.discard('b') # {}
my_set.discard('b') # {} (no error)

#lookup

my_set = {'a'}

'a' in my_set # True
'b' in my_set # False



