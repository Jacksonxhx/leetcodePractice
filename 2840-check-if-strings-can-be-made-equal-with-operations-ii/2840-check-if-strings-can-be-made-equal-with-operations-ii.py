class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        hash统计奇偶数位的出现个数，如果一样就可以
        """
        hasht1 = {0: [], 1: []}
        hasht2 = {0: [], 1: []}
        n = len(s1)
        
        for i in range(n):
            if i % 2 == 0:
                hasht1[0].append(s1[i])
                hasht2[0].append(s2[i])
            else:
                hasht1[1].append(s1[i])
                hasht2[1].append(s2[i])
        
        return sorted(hasht1[0]) == sorted(hasht2[0]) and sorted(hasht1[1]) == sorted(hasht2[1])