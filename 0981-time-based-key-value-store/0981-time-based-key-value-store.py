from collections import OrderedDict

class TimeMap:

    def __init__(self):
        self.hash = OrderedDict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = []
        
        self.hash[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # 用二分找最大值
        if key not in self.hash:
            return ""
        
        tmp = self.hash[key]
        l, r = 0, len(tmp)
        while l < r:
            mid = (l + r) // 2
            if tmp[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid
        return tmp[l-1][0] if l > 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)