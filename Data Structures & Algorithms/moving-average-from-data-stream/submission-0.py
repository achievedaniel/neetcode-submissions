class MovingAverage:

    def __init__(self, size: int):
        self.size = []
        self.window = size

    def next(self, val: int) -> float:
        self.size.append(val)
        divideBy = len(self.size) if len(self.size) < self.window else self.window
        
        return sum(self.size[-self.window:]) / divideBy
        

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
