class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        backtracking
        n外层
        k里层
        """
        res = []
        
        def backtrack(tmp, index):
            if len(tmp) == k:
                res.append(tmp[:])
            else:
                # 从1开始到n
                for i in range(index, n + 1):
                    # tmp加上i
                    tmp.append(i)
                    # 然后一个个枚举
                    backtrack(tmp, i + 1)
                    # 回溯，移除上一个元素
                    tmp.pop() 

        backtrack([], 1)
        return res