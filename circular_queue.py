class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.front = -1
        self.rear = -1
        self.capacity = k

    def enqueue(self, value):
        if (self.rear + 1) % self.capacity == self.front:
            return False
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = value
        return True

    def dequeue(self):
        if self.front == -1:
            return False
        
        removed_value = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return removed_value

    def getFront(self):
        if self.front == -1:
            return None
        else:
            return self.queue[self.front]

    def getRear(self):
        if self.rear == -1:
            return None
        else:
            return self.queue[self.rear]

    def isEmpty(self):
        return self.front == -1
        
    def isFull(self):
        if (self.rear + 1) % self.capacity == self.front:
            return True
        else:
            return False
        
cq = CircularQueue(3)
print(cq.isEmpty())  
print(cq.enqueue(10))  
print(cq.enqueue(20))  
print(cq.enqueue(30))  
print(cq.enqueue(40))  
print(cq.getFront())   
print(cq.getRear())    
print(cq.dequeue())    
print(cq.getFront())   
print(cq.enqueue(40))  
print(cq.getRear())    
print(cq.isFull())     


