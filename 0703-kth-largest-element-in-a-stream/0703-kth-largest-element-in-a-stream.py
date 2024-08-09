import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        # 把所有的k之外的pop掉
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        # 如果缺element
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        # 如果不缺
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)