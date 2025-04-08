#Hashing and Bucketing:
#When an element is added to a hash set, 
# it is processed by a hash function that 
# produces a numeric hash value. This value 
# is then mapped to an index in an underlying 
# array (the bucket index). Each bucket can 
# hold multiple elements that may hash to 
# the same index.

class hashSet():

    #the __init__ method creates these buckets to 
    # prepare for future insertions, ensuring 
    # that every element can be quickly accessed 
    # or inserted even if some hash collisions occur
    def __init__(self, initial_capacity):
        buckets = [[] for _ in range(initial_capacity)]
        self.buckets = buckets
        self.capacity = initial_capacity
        self.size = 0

    def add(self, element):
        hash_code = hash(element) #create the hash value
         #divide the hash_code by the number of buckets with the remainder being the bucket
        index = abs(hash_code) % self.capacity 
            
        #check the bucket for a matching hashcode
        bucket = self.buckets[index]
        if element in bucket:
            return
            
        #Add the Element and Increment the Size
        bucket.append(element)
        self.size += 1

        # Check Load Factor and Resize If Needed
        # load_factor tells you how "full" your hash set is
        #If too many elements are stored (e.g. more than 75% 
        # full), collisions become more frequent

        load_factor = self.size / self.capacity
        if load_factor > 0.75:
            self.resize(self.capacity * 2)  #create more buckets


    def remove(self, element):
        hash_code = hash(element)
        index = abs(hash_code) % self.capacity #determine the correct bucket index
        bucket = self.buckets[index] #Access the bucket at that index.

        if element in bucket:
            bucket.remove(element)
            self.size -= 1


    def contains(self, element):
        hash_code = hash(element)
        index = abs(hash_code) % self.capacity #determine the correct bucket index
        bucket = self.buckets[index] #Access the bucket at that index.

        if element in bucket:
            return True
        else:
            return False

        #When your hash set starts to get full (too many elements relative 
        # to the number of buckets), more elements get hashed into the 
        # same buckets.

    def resize(self, new_capacity): #increase the number of buckets 
        #Create a new list of empty buckets with length = new_capacity
        new_buckets = [[] for _ in range(new_capacity)]

        for bucket in self.buckets:
            for element in bucket:
                hash_code = hash(element)
                index = abs(hash_code) % new_capacity #determine the correct bucket index
                new_buckets[index].append(element) #Insert the element into the corresponding new bucket

        #Replace the old buckets with the new ones and update capacity
        self.buckets = new_buckets
        self.capacity = new_capacity



print("TEST 1: Add and Contains =====")
s = hashSet(4)
s.add("apple")
s.add("banana")
s.add("cherry")

print("Contains 'apple':", s.contains("apple"))   
print("Contains 'banana':", s.contains("banana")) 
print("Contains 'cherry':", s.contains("cherry")) 
print("Contains 'date':", s.contains("date"))     
print("Current size:", s.size)
print()

print("TEST 2: Add Duplicate =====")
s.add("banana")  
print("Re-added 'banana'")
print("Current size (should still be 3):", s.size)
print()

print("TEST 3: Remove Element =====")
s.remove("banana")
print("Removed 'banana'")
print("Contains 'banana':", s.contains("banana")) 
print("Current size:", s.size)
print()

print("TEST 4: Remove Nonexistent Element =====")
s.remove("pineapple")  
print("Tried to remove 'pineapple' (not in set)")
print("Current size (should remain unchanged):", s.size)
print()

print("TEST 5: Trigger Resize =====")
s.add("date")
s.add("elderberry")  
print("Added 'date' and 'elderberry'")
print("Contains 'date':", s.contains("date"))         
print("Contains 'elderberry':", s.contains("elderberry")) 
print("Current size:", s.size)
print("Current capacity:", s.capacity)
print()
