class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty!"
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty!"
        
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        print("Front ->", self.items, "<- Rear")
    
test = Queue()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)

test.display()

print("Dequeued: ", test.dequeue())

test.display()

# print(test.peek())



#######################################

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty!"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty!"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Front ->", self.items, "<- Rear")

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
print("Dequeued: ", q.dequeue())
q.display()

