class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        先计算距离，然后keep update maxCost看substring
        """
        distance = []
        n = len(s)
        for i in range(n):
            distance.append(abs(ord(t[i]) - ord(s[i])))
        
        res, i = 0, 0
        cur_cost = 0
        for j in range(n):
            cur_cost += distance[j]
            
            while cur_cost > maxCost:
                cur_cost -= distance[i]
                i += 1
            
            res = max(res, j - i + 1)
            
        return res
            