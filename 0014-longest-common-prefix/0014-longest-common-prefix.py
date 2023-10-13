'''
思路：

1. 首先创建一个res数组存放strs[0]
2. 遍历整个strs，和res逐字对比
3. 如果有不同，continue当前循环，并且res[0:当前位置]
4. 遍历完之后输出
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1: return ""
        res = strs[0]
        for str in strs:
            i = 0
            while i < len(res) and i < len(str) and res[i] == str[i]:
                i += 1
            res = res[:i]
        return res