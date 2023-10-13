class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #去除空数组情况
        if len(nums) < 1: return 0  
        #应对当target大于数组中最大值时
        if target > nums[len(nums) - 1]: return len(nums)
        #二分查找
        l = 0   #左下标
        r = len(nums) - 1   #右下标
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l
        