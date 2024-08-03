class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        用单调栈做On
        通过计算每个元素在所有子数组中作为最大值和最小值的贡献
        然后将这些贡献进行汇总来得到最终的结果
        """
        res = 0
        inf = float("inf")
        
        s = []
        A = [-inf] + nums + [-inf]
        # 计算每个元素被当作最小值的在所有存在subarray的贡献
        for i, x in enumerate(A):
            # 当stack存在且栈顶不是最小存在
            while s and A[s[-1]] > x:
                # 栈顶元素的index
                j = s.pop()
                # 弹出后栈顶元素索引
                k = s[-1]
                # res = i到j结尾的，j到k结尾的最小值贡献
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
        
        A = [inf] + nums + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        
        return res