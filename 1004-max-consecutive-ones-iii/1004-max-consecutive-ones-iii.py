class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        维护一个滑动窗口，这个窗口最多有k个0
        最后返回最大的窗口size
        '''
        n = len(nums)
        cnt_zero = 0
        l, r = 0, 0
        res = 0
        
        while r < n:
            if nums[r] == 0:
                cnt_zero += 1
                
            while cnt_zero > k:
                if nums[l] == 0:
                    cnt_zero -= 1
                
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res
        
                        
                
            