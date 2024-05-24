class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        先排序然后看前后是否相等
        '''
        
        nums = sorted(nums)

        i = 0
        while i < len(nums) - 1:
            j = i + 1
            if nums[i] == nums[j]:
                i += 2
            else:
                return nums[i]
        
        return nums[i]