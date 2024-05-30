class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hasht = Counter(arr)
        res = []
        
        for key, value in hasht.items():
            res.append(value)
            
        return len(res) == len(set(res))