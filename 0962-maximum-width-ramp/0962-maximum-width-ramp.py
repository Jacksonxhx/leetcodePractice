class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # 首先从左到右遍历一个单调递减栈
        # 然后从右到左遍历找到最大宽度
        stack = []
        length = len(nums)
        max_width = 0
        
        for i in range(length):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # 从右往左找最大
        for j in range(length - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                index = stack.pop()
                max_width = max(max_width, j - index)
                
        return max_width