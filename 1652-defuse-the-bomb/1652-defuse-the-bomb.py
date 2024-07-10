class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        
        if k == 0:
            return [0] * length
        
        res = [0] * length
        code = code * 2
        
        if k > 0:
            for i in range(length):
                res[i] = sum(code[i+1:i+1+k])
        else:
            for i in range(length):
                res[i] = sum(code[i+length+k:i+length])
                
        return res