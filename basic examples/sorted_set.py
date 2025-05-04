#insertion

from sortedcontainers import SortedSet

my_set = SortedSet()

my_set.add(90)
my_set.add(80)
my_set.add(85)

print(my_set) # SortedSet([80, 85, 90])


#deletion

my_set = SortedSet([90, 80, 85, 95])

my_set.remove(90) # SortedSet([80, 85, 95])

my_set.discard(100) # SortedSet([80, 85, 95]) 

my_set.pop() # 95

my_set.pop(0) # 80

print(my_set) # SortedSet([85])

my_set.clear() # SortedSet([])


#lookup

my_set = SortedSet([80, 85, 90])

does_a_exist = 'a' in my_set # True
does_b_exist = 'b' in my_set # False



#iterating

sorted_set = SortedSet([4, 3, 5, 2, 1])

for num in sorted_set:
    print(num)  # 1, 2, 3, 4, 5
