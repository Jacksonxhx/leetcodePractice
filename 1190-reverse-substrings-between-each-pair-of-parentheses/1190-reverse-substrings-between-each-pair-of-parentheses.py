class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 首先记录括号位置
        opened = []
        pair = {}
        
        for i, c in enumerate(s):
            if c == '(':
                opened.append(i)
            if c == ')':
                # 最近的'('
                j = opened.pop()
                pair[i], pair[j] = j, i
        
        # 翻转
        res = []
        # i表示索引，d表示方向
        i, d = 0, 1
        while i < len(s):
            if s[i] in '()':
                # (的话找到)，)的话找到(
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            # 更新位置
            i += d
        
        return ''.join(res)