class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            n_1 = len(str1)
            n_2 = len(str2)
            return str1 == str2[:n_1] and str1 == str2[n_2-n_1:]
        
        cnt = 0
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]) == True:
                    cnt += 1
                    
        return cnt