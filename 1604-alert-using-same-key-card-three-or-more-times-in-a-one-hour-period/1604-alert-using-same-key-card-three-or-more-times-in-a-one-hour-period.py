from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hasht = defaultdict(list)
        for i in range(len(keyName)):
            time = int(keyTime[i].split(":")[0]) * 60 + int(keyTime[i].split(":")[1]) 
            hasht[keyName[i]].append(time)
        
        res = []
        for key, value in hasht.items():
            value.sort()
            for i in range(2, len(value)):
                if value[i] - value[i - 2] <= 60:
                    res.append(key)
                    break
        
        return sorted(res)