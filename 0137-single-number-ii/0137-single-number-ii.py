class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        i = 0
        
        while i < len(nums) - 2:
            if nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
                i += 3
            else:
                return nums[i]
        
        return nums[i]