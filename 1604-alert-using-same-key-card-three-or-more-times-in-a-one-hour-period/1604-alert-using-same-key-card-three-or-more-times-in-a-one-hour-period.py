from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hasht = defaultdict(list)
        
        for i in range(len(keyName)):
            time = int(keyTime[i].split(":")[0]) * 60 + int(keyTime[i].split(":")[1]) 
            hasht[keyName[i]].append(time)
        
        res = [] 
        
        for key, value in hasht.items():
            # 首先对时间列表进行排序，以确保时间是按顺序排列的
            value.sort()
            
            # 从第三个时间点开始，检查当前时间与前两个时间的差是否在60分钟以内
            for i in range(2, len(value)):
                if value[i] - value[i - 2] <= 60:
                    res.append(key)
                    break 
        
        return sorted(res)
