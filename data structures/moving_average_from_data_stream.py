class MovingAverage:
    def __init__(self, size: int):
        self.queue = []
        self.total_sum = 0
        self.size = size
    
    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.total_sum -= self.queue.pop(0)

        self.queue.append(val)
        self.total_sum += val

        return self.total_sum / min(len(self.queue), self.size)


moving_average = MovingAverage(3)

print(moving_average.next(1))
print(moving_average.next(10))
print(moving_average.next(3))
print(moving_average.next(5))
print(moving_average.next(15))
print(moving_average.next(52))
print(moving_average.next(4))
print(moving_average.next(7))
