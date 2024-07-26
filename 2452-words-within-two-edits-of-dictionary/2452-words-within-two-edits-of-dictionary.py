class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        res = []
        
        for query in queries:
            for word in dictionary:
                tmp = 0
                for i in range(len(word)):
                    if query[i] != word[i]:
                        tmp += 1
                if tmp <= 2:
                    res.append(query)
                    break
        
        return res