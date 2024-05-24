class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        用位运算的XOR做
        '''
        if len(nums) == 1:
            return nums[0]
        
        ans = 0
        for i in nums:
            ans ^= i
        
        return ans