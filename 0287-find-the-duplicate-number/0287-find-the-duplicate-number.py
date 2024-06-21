class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        用binary search做，统计小于等于nums的数cnt
        如果cnt <= mid，则重复数一定不会出现在左侧区间，那么从右侧区间开始搜索
        反之重复的数在左边
        '''
        # 因为数的区间在这个范围里
        n = len(nums) - 1
        l, r = 1, n
        
        while l < r:
            mid = (l + r) // 2
            cnt = 0
            
            # 统计cnt
            for num in nums:
                if num <= mid:
                    cnt += 1
            
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid
        
        return l