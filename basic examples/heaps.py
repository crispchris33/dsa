import heapq

heap = [] # min heap

heapq.heappush(heap, 3)
heapq.heappush(heap, 1)

print(heap[0])  # 1

heapq.heappush(heap, 0)

print(heap[0])  # 0


#create empty list to use heaps
#push elements 3, 1 into the heap
#heaps arrange smallest value to largest
#access at zero returns 1
#add value 0 to the heap
#acces again returns zero at index 0

#minimum heap by default


#remove elements with 

heapq.heappop()

#removes lowest priority

