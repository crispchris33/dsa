# leftChild of i = heap[2 * i]
# rightChild of i = heap[(2 * i) + 1] 
# parent of i = heap[i // 2]

class Heap:
    def __init__(self):
        self.heap = [0]