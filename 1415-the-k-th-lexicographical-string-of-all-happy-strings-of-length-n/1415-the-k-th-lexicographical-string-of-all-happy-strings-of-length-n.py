class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        path = []
        
        def backtrack(i):
            if i == n:
                res.append(''.join(path))
                return
            
            for c in 'abc':
                if not path or path[-1] != c:
                    path.append(c)
                    backtrack(i + 1)
                    path.pop()
        
        backtrack(0)
        
        res = sorted(res)
        return res[k - 1] if k <= len(res) else ""