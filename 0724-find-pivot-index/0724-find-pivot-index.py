class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        sumleft = [0] * length
        sumright = [0] * length
        
        for i in range(1, length):
            sumleft[i] = sumleft[i - 1] + nums[i - 1]
        
        nums_reverse = nums[::-1]
        
        for i in range(1, length):
            sumright[i] = sumright[i - 1] + nums_reverse[i - 1]
        sumright = sumright[::-1]
        
        for i in range(length):
            if sumleft[i] == sumright[i]:
                return i
        
        return -1