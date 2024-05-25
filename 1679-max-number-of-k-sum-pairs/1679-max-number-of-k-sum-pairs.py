class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        先sorted(nums)然后双指针前后走找pair，O(n)
        '''
        nums = sorted(nums)
        i, j = 0, len(nums) - 1
        res = 0
        
        while i < j:
            # 处理找到pair的情况
            if nums[i] + nums[j] == k:
                res += 1
                i += 1
                j -= 1
            # 处理i向后移动的情况
            elif k - nums[i] > nums[j]:
                i += 1
            # 处理j向前移动的情况
            elif nums[i] + nums[j] > k:
                j -= 1
        
        return res