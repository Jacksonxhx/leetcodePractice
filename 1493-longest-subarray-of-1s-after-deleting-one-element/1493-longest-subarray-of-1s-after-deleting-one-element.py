class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        只可以删一个element，所以构造一个只有一个0的滑动窗口
        '''
        l, r, res = 0, 0, 0
        cnt = 0
        
        while r < len(nums):
            if nums[r] == 0:
                cnt += 1
            
            while cnt > 1:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            
            if r - l + 1 > res:
                res = r - l + 1
            
            r += 1
 
        return res - 1