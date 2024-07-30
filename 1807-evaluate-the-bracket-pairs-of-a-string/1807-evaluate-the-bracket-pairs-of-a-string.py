class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        s_list = list(s)
        hasht = dict()
        for key, value in knowledge:
            hasht[key] = value
        
        tmp = ''
        res = ''
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                while s[i] != ')':
                    tmp += s[i]
                    i += 1
                if tmp in hasht:
                    res += hasht[tmp]
                else:
                    res += '?'
                tmp = ''
            elif s[i] != ')':
                res += s[i]
            i += 1
        
        return res