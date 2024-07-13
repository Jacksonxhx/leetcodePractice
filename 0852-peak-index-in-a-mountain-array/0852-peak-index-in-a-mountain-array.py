class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        peak就是下一个小于上一位
        满足右边的性质，所以区间被分为[l, mid] 和 [mid + 1, r]
        """
        l, r = 0, len(arr) - 1
        
        # 区间分为[l, mid] 和 [mid + 1, r]
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid + 1
        
        return l
            