class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        不定长度的sliding window，快慢指针维护
        根据target大小判断
        '''
        l, r = 0, 0
        ans = float('inf')
        cursum = 0
        
        while r < len(nums):
            cursum += nums[r]
            
            # 当窗口需要缩小的时候
            while cursum >= target:
                # 每次当cursum >= target时，记录ans
                ans = min(ans, r - l + 1)
                cursum -= nums[l]
                l += 1
            
            r += 1
        
        return 0 if ans == float('inf') else ans