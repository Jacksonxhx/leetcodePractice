class Solution:
    def simplifyPath(self, path: str) -> str:
        sp = path.split('/')
        clean = []
        for item in sp:
            if item != '':
                clean.append(item)
        
        stack = [0] * len(path)
        pos = 0
        
        for i in range(0, len(clean)):
            
            if clean[i] == '.':
                continue
            
            if clean[i] == '..':
                if pos - 2 < 0:
                    continue
                pos -= 2
                stack[pos] = 0
                stack[pos + 1] = 0
                continue
            
            # 如果不是操作符，append
            stack[pos] = '/'
            stack[pos + 1] = clean[i]
            pos += 2
        
        res = ''
        for item in stack:
            if item != 0:
                res += item
        
        if len(res) == 0:
            res = '/'
        
        return res