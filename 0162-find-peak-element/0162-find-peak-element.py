class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        当时间复杂度是O(logn)时，可以使用二分查找来做
        做双指针l, r，然后从中间开始往外找
        如果mid < mid + 1，则峰值在右边
        如果mid >= mid + 1，则峰值在左边
        当l >= r的时候return
        
        核心思路就是，通过二分确定了一边的大小顺序，只需要看另一边来判断
        """
        # 设定双指针
        l = 0
        r = len(nums) - 1
        while l < r:
            # //表示整数除法向下取整，一直找到中点
            mid = (l + r) // 2
            # 判断峰值是在左还是右
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l