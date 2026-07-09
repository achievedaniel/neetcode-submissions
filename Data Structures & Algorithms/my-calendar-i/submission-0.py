class MyCalendar:
    
    def __init__(self):
        self.day = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.day:
            if startTime < e and endTime > s:
                return False
        self.day.append((startTime,endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)