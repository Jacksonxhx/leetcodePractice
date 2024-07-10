import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        每轮把小于等于w的放到queue，找到一个max，然后用visited追踪
        使用一个最大堆和一个最小堆，分别存储可以做的项目和还不能做的项目
        """
        min_capital_heap = []
        for i in range(len(profits)):
            # 用最小堆存capital最小的
            heapq.heappush(min_capital_heap, (capital[i], profits[i]))
        
        
        # 用最大堆存可以做的项目的利润
        max_profit_heap = []
        
        # 总共做k轮
        for _ in range(k):
            # 把所有当前w可以做的项目放入最大堆
            while min_capital_heap and min_capital_heap[0][0] <= w:
                cap, profit = heapq.heappop(min_capital_heap)
                # 用-数模拟最大堆
                heapq.heappush(max_profit_heap, -profit)
            
            # 如果没有可以做的项目，直接返回
            if not max_profit_heap:
                break
            
            # 选择利润最大的项目
            w += -heapq.heappop(max_profit_heap)
        
        return w
        