class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        hasht = dict()
        size = len(words)
        res = 0
        
        for i in range(size):
            hasht[i] = False
        
        for i in range(size):
            if hasht[i]:
                continue
            for j in range(i + 1, size):
                if hasht[j]:
                    continue
                if words[i] == words[j][::-1]:
                    res += 1
                    hasht[i] = True
                    hasht[j] = True
        
        return res