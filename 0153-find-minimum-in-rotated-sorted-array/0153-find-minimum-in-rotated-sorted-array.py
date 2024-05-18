class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        用二分
        设定left，right分别指向数组的最左和最右
        然后跟mid对比找区间
        
        如果nums[mid] > nums[right]，则最小值在mid右边
        如果nums[mid] <= nums[right]，则最小值在mid或mid左边
        '''
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]