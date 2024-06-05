class RecentCounter:

    def __init__(self):
        self.requests = []
        self.index = 0

    def ping(self, t: int) -> int:        
        self.requests.append(t)
        
        while self.requests[self.index] and self.requests[self.index] < (t-3000):
            self.index += 1
        
        return len(self.requests) - self.index


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)