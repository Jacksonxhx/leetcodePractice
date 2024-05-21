class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. 从右找到第一个pviot，确保pivot右侧都是升序的
        2. 交换successor和pivot，然后reverse pivot右边的可以保证我们得到的是比当前排列大的最小排列
        因为右侧从升序变成了降序
        """
        n = len(nums)
        if n <= 1:
            return
        
        # Step 1: Find the first decreasing element from the end
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        
        if pivot >= 0:  # If there is a valid pivot
            # Step 2: Find the first element larger than pivot from the end
            
            successor = n - 1
            while successor >= 0 and nums[successor] <= nums[pivot]:
                successor -= 1
            
            # Step 3: Swap pivot and successor
            nums[pivot], nums[successor] = nums[successor], nums[pivot]
            
        # Step 4: Reverse the elements from pivot + 1 to end
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1