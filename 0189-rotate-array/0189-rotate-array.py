class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate = k % len(nums)
        location = len(nums) - rotate
        res = []
        while location < len(nums):
            res.append(nums[location])
            location += 1
        
        for i in range(len(nums) - rotate):
            res.append(nums[i])
        
        for i in range(len(nums)):
            nums[i] = res[i]