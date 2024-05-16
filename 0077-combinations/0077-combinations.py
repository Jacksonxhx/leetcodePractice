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
                if len(set(tmp)) != k:
                    return
                res.append(tmp[:])
            else:
                for i in range(index, n + 1): 
                    tmp.append(i)
                    backtrack(tmp, i + 1)
                    tmp.pop() # 回溯，移除最后一个元素

        backtrack([], 1)
        return res