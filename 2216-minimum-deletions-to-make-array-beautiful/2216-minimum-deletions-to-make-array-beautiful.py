class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deletions = 0
        i = 0
        
        while i < len(nums) - 1:
            # 满足beautiful
            if nums[i] == nums[i + 1] and (i - deletions) % 2 == 0:
                deletions += 1 
            else:
                i += 1 
            
            i += 1  # Continue to the next element
        
        # 处理结尾
        if (len(nums) - deletions) % 2 == 1:
            deletions += 1
        
        return deletions