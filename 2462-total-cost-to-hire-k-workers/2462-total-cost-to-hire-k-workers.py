import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
        用左右两个，大小为candidates的min_heap去维护，然后每次pop看结果
        """
        n = len(costs)
        if n == 0 or k == 0 or candidates == 0:
            return 0
        
        min_heap_l = []
        min_heap_r = []
        res = 0
        
        # 初始的索引
        left = 0
        right = n - 1
        
        # 建左小根堆
        for i in range(candidates):
            if left <= right:
                heapq.heappush(min_heap_l, (costs[left], left))
                left += 1
        
        # 建右小根堆
        for i in range(candidates):
            if left <= right:
                heapq.heappush(min_heap_r, (costs[right], right))
                right -= 1
        
        # 选择k个最小代价的工人
        for _ in range(k):
            if not min_heap_r or (min_heap_l and min_heap_l[0][0] <= min_heap_r[0][0]):
                cost, idx = heapq.heappop(min_heap_l)
                res += cost
                if left <= right:
                    heapq.heappush(min_heap_l, (costs[left], left))
                    left += 1
            else:
                cost, idx = heapq.heappop(min_heap_r)
                res += cost
                if left <= right:
                    heapq.heappush(min_heap_r, (costs[right], right))
                    right -= 1
        
        return res