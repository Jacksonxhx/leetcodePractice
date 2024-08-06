class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # 设定一个hasht存pieces对应的list，用开头存
        mp = {x[0]:x for x in pieces}
        
        res = []
        
        for num in arr:
            res += mp.get(num, [])
        
        return res == arr
        