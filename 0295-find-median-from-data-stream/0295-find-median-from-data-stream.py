import heapq
class MedianFinder:

    def __init__(self):
        # 大根堆存小于中位数的值
        self.small = []
        # 小根堆存大于中位数的值
        self.large = [] 
        

    def addNum(self, num: int) -> None:
        # 首先统一到中位数左侧的大根堆
        heapq.heappush(self.small, -num)
        # 判断大根堆顶是否大于小根堆顶，如果是，把median左侧的第一个放到右侧保持顺序
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()