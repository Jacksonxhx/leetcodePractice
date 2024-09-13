class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 5:
            return 0
        
        nums.sort()
        
        # 考虑移除最多3个元素的四种情况
        return min(nums[-1] - nums[3],  # 移除前3个元素
                   nums[-2] - nums[2],  # 移除前2个元素和最后1个
                   nums[-3] - nums[1],  # 移除前1个元素和最后2个
                   nums[-4] - nums[0])  # 移除最后3个元素