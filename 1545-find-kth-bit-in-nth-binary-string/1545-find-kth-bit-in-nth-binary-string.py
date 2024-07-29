class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        res = '0'
        
        for _ in range(n):
            tmp = list(res)
            for i in range(len(tmp)):
                if tmp[i] == '1':
                    tmp[i] = '0'
                elif tmp[i] == '0':
                    tmp[i] = '1'
            res = res + '1' + ''.join(reversed(tmp))
            
        return res[k-1]