class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        """
        使用前后前缀合+单调栈
        单调栈是用来维护一个稳定上升的序列
        前后缀的意义是找到当前i位置作为peek的最大0-(i-1)的和
        """
        n = len(heights)
        suf = [0] * (n + 1)
        # 单调栈
        st = [n]
        s = 0
        
        # 从后往前compute suffix
        for i in range(n - 1, -1, -1):
            # 
            x = heights[i]
            # 当stack存在且当前x小于栈顶
            # 从栈顶弹出所有比 x 大的元素，更新栈中的元素和 s 的值。
            while len(st) > 1 and x <= heights[st[-1]]:
                j = st.pop()
                s -= heights[j] * (st[-1] - j)
            s += x * (st[-1] - i)  # 从 i 到 st[-1]-1 都是 x
            # 更新后缀和
            suf[i] = s
            # 更新栈
            st.append(i)
        
        ans = s
        # 从前往后的栈
        st = [-1]
        pre = 0
        for i, x in enumerate(heights):
            while len(st) > 1 and x <= heights[st[-1]]:
                j = st.pop()
                pre -= heights[j] * (j - st[-1])  # 撤销之前加到 pre 中的
            pre += x * (i - st[-1])  # 从 st[-1]+1 到 i 都是 x
            ans = max(ans, pre + suf[i + 1])
            st.append(i)
        return ans