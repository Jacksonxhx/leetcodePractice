class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        维护一个滑动窗口，这个窗口最多有k个0
        最后返回最大的窗口size
        '''
        left, right, res = 0, 0, 0
        # cnt记录有多少个0
        cnt = 0
        
        while right < len(nums):
            # 如果遇到0，cnt++
            if nums[right] == 0:
                cnt += 1
            
            # 当cnt > k, left右移
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            
            res = max(res, right - left + 1)
            
            right += 1
            
        return res
                        
                
            