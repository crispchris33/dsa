class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        self.queue.append((item, priority))
        
    def pop(self):
        if self.queue:
            max_index = 0
            i = 1
            while i < len(self.queue):
                if self.queue [i][1] > self.queue[max_index][1]:
                    max_index = i
                i += 1
            return self.queue.pop(max_index)[0]
        else:
            return None
    
    def peek(self):
        if self.queue:
            max_index = 0
            i = 1
            while i < len(self.queue):
                if self.queue[i][1] > self.queue[max_index][1]:
                    max_index = i
                i += 1
            return self.queue[max_index]
        else:
            return None

    def empty(self):
        return len(self.queue) == 0
    



pq = PriorityQueue()

print(pq.empty())  # True

pq.push('a', 5)
pq.push('b', 2)
pq.push('c', 3)
print(pq.queue)
print(pq.empty())

print(pq.peek())
print(pq.pop())
print(pq.peek())
print(pq.pop())
print(pq.pop())
print(pq.empty())
print(pq.pop())
print(pq.peek())
