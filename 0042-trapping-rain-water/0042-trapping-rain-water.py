class Solution:
    def trap(self, height: List[int]) -> int:
        """
        用monastic stack做
        """
        ans = 0
        stack = []
        size = len(height)
        for i in range(len(height)):
            # 当stack还有且当前height大于栈顶元素
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()
                # 栈顶index是左边的边界，i是右边的边界
                if stack:
                    # 栈顶下一个
                    left = stack[-1] + 1
                    # 当前上一个
                    right = i - 1
                    # 左右边界去最低，然后-目前为止的height，就是能存多少雨水
                    high = min(height[i], height[stack[-1]]) - height[cur]
                    ans += high * (right - left + 1)
                else:
                    break
                
            # 如果当前height小于栈顶存index
            stack.append(i)
        
        return ans