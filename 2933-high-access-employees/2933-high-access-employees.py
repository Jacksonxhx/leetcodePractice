class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        """
        hash存list，排序看i，j差值
        """
        hasht = defaultdict(list)
        res = []
        
        for key, value in access_times:
            hasht[key].append(int(value[:2]) * 60 + int(value[2:]))
        
        for key, value in hasht.items():
            k = len(value)
            if k < 3:
                continue
            
            value = sorted(value)
            
            is_high = False

            for i in range(k - 2):
                is_high |= value[i + 2] < value[i] + 60

            if is_high:
                res.append(key)
        
        return res
            
            