class Queue:
    def __init__(self):
        self.items = []

    def add_doc(self, item):
        self.items.append(item)


    def print_doc(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Print queue is empty."
    

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty!"
        
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
            print(self.items)

    def auto_queue(self):
        while not self.is_empty():
            print("Printing.... ", self.items[0])
            self.items.pop(0)
        print("All documents have been printed.")


test = Queue()
test.add_doc('doc1.txt')
test.add_doc('doc2.txt')
test.add_doc('doc3.txt')

test.display()

test.auto_queue()

# print("Printing.... ", test.print_doc())
# print("Printing.... ", test.print_doc())
# print("Printing.... ", test.print_doc())
# print("Printing.... ", test.print_doc())

test.display()