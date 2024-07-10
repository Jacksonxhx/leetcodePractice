class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        用两个栈存，计算每个元素左边和右边分别有多少个连续的元素都大于该元素，从而确定以该元素为最小值的子数组数量
        """
        mod = 10**9 + 7
        n = len(arr)
        
        # 前一个小于当前元素的索引
        prev_less = [-1] * n
        # 后一个小于当前元素的索引
        next_less = [n] * n
        
        stack = []
        
        # 计算prev_less数组
        for i in range(n):
            # 当栈顶大于arr[i]，弹出
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        
        # 计算next_less数组
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)
            
        # 计算结果
        res = 0
        for i in range(n):
            left_count = i - prev_less[i]
            right_count = next_less[i] - i
            res = (res + arr[i] * left_count * right_count) % mod
        
        return res