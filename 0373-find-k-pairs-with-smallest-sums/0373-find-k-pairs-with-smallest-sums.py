class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        维护一个size为k的小根堆
        因为两个数组都是从小到大排列的，所以先从任意一个数组的第一位开始固定
        
        """
        if k <= 0 or not nums1 or not nums2:
            return []
        
        min_heap = []
        # 初始化堆，将 nums1 的前k个元素和 nums2 的第一个元素配对
        for i in range(min(k, len(nums1))):
            # heapq的用法需要整理一下
            # 这里就是把min_heap中加入一个元组()
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        result = []
        # 维护一个小根堆，获取k对最小值
        while k > 0 and min_heap:
            # pop min_heap中的最小值，这里是按照元组的第一个值排序
            sum_val, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1
            # 如果 nums2 还有下个元素，继续配对
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result
        
        
        
        
        
        