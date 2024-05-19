class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        
        def backtracking(symbol, index):
            # base case, 每当path满之后加入res
            if 2 * n == index:
                if symbol == 0:
                    res.append("".join(path))
                    return
            else:
                if symbol < n:
                    path.append('(')
                    backtracking(symbol + 1, index + 1)
                    path.pop()
                if symbol > 0:
                    path.append(')')
                    backtracking(symbol - 1, index + 1)
                    path.pop()
        
        backtracking(0, 0)
        return res
            