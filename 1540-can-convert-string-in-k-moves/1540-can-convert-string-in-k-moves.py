class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)
        cnts = [0] * n
        
        # 记录每个差值出现的次数
        diff_count = Counter()
        
        for i in range(n):
            diff = (ord(t[i]) - ord(s[i])) % 26
            if diff > 0:
                diff_count[diff] += 1
        
        # 检查每个差值的可行性
        for diff, count in diff_count.items():
            # 每个diff需要的最大次数为 (count - 1) * 26 + diff
            if (count - 1) * 26 + diff > k:
                return False
        
        return True