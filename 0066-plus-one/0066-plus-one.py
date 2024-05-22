class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strd = ''
        for i in digits:
            strd += str(i)
        num = int(strd)
        num += 1
        
        res = []
        
        num = str(num)
        
        for i in num:
            res.append(int(i))
            
        return res