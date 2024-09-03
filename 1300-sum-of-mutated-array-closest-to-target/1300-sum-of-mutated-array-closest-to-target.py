class Solution:
    def lower_bound(self, arr, value):
        """寻找第一个大于等于value的元素的下标"""
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < value:
                l = mid + 1
            else:
                r = mid
        return l
    
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        
        # 计算前缀和数组
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
        
        # 二分查找
        l, r = 0, arr[-1]
        closest_value, min_diff = 0, float('inf')
        
        while l <= r:
            mid = (l + r) // 2
            
            # 找到第一个大于等于mid的元素的下标
            index = self.lower_bound(arr, mid)
            
            # 计算替换后的数组和
            current_sum = prefix_sum[index] + (n - index) * mid
            diff = abs(current_sum - target)
            
            if diff < min_diff or (diff == min_diff and mid < closest_value):
                closest_value = mid
                min_diff = diff
            
            if current_sum < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return closest_value 
        