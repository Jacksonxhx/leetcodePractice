class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        # 如果遇到len partition == 1 还 < k 直接break
        # greedy能大就大
        res = 0
        i = 0
        n = len(s)
        
        while i < n:
            # 尝试找到尽量长的子串
            j = i
            while j < n and int(s[i:j+1]) <= k:
                j += 1
            
            # 如果找不到直接break
            if j == i:
                return -1
            
            # 如果找到，直接更新，res++
            i = j
            res += 1
        
        return res