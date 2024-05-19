class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        根据symbol在不同index中决定选择'('还是')'填入
        '''
        res = []
        path = []
        
        def backtracking(symbol, index):
            # base case, 每当path满之后加入res
            if 2 * n == index:
                # 需要确定'('和')'的数量一样
                if symbol == 0:
                    res.append("".join(path))
                    return
            # 分类分情况讨论
            else:
                # 当'('的数量小于n个时append
                if symbol < n:
                    path.append('(')
                    backtracking(symbol + 1, index + 1)
                    path.pop()
                # 当')'的数量小于'('的数量时
                if symbol > 0:
                    path.append(')')
                    backtracking(symbol - 1, index + 1)
                    path.pop()
        
        backtracking(0, 0)
        return res
            