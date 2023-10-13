class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) < 1: return 0 
        if target > nums[len(nums) - 1]: return len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l
        