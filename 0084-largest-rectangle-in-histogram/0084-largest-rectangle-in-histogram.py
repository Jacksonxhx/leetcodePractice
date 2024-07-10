class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        遍历整个柱体，遇到小的pop，算体积
        """
        # 确保最后都会弹出
        heights.append(0)
        res = 0
        stack = []
        
        for i in range(len(heights)):
            # 当有栈且新柱小于栈顶时
            while stack and heights[i] <= heights[stack[-1]]:
                cur = stack.pop()
                # 左边的边界，栈顶右一个
                left = stack[-1] + 1 if stack else 0
                # 右边的边界，当前前一个
                right = i - 1
                # 更新最大面积，底 + 1
                res = max(res, (right - left + 1) * heights[cur])
            stack.append(i)
        
        return res