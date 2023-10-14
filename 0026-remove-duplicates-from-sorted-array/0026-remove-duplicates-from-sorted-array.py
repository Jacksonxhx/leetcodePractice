class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        index = 0
        tmp = [0] * size
        
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] != nums[i + 1]:
                tmp[index] = nums[i]
                index += 1
            elif i == len(nums) - 1:
                tmp[index] = nums[i]
                index += 1
        
        for i in range(index):
            nums[i] = tmp[i]
                
        return index