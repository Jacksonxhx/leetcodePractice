from collections import defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        
        for word in words2:
            word_count = Counter(word)
            for ch in word_count:
                max_freq[ch] = max(max_freq[ch], word_count[ch])

        res = []

        for word in words1:
            
            word_count = Counter(word)
            is_universal = True
            
            for ch in max_freq:
                if word_count[ch] < max_freq[ch]:
                    is_universal = False
                    break
                    
            if is_universal:
                res.append(word)
        
        return res