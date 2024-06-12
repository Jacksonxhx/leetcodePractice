class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasht = Counter(nums)
        sorted_by_values = dict(sorted(hasht.items(), key=lambda item: item[1], reverse=True))
        res = []
        
        for key, value in sorted_by_values.items():
            if k == 0:
                break
            res.append(key)
            k -= 1
            
        return res