import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        维护一个大小为k的小根堆，root是第k大的数
        """
        res = []
        for num in nums:
            if len(res) < k:
                heapq.heappush(res, num)
            elif len(res) == k and res[0] < num:
                heapq.heappop(res)
                heapq.heappush(res, num)
        return heapq.heappop(res)
                
        
        