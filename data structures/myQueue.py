class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            return 
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            return 
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue) 
    

q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.dequeue())
print(q.peek())
print(q.is_empty())
print(q.dequeue())
print(q.is_empty())
print(q.size())
q.enqueue(1)
q.enqueue(2)
print(q.peek())
print(q.size())
