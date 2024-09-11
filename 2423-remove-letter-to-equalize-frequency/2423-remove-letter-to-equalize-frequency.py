from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(word)
        freq = Counter(cnt.values())
        print(freq)
        
        # 如果所有字符频率相同，并且只有一个不同的频率
        if len(freq) == 1:
            # 所有频率都是 1，删除一个字符后剩下的字符频率可以保持相同
            return list(freq.keys())[0] == 1 or freq[list(freq.keys())[0]] == 1
        
        # 如果有两个不同的频率
        if len(freq) == 2:
            f1, f2 = list(freq.keys())
            
            # 频率差为 1，并且频率较高的那个只出现了一次
            if (f1 == f2 + 1 and freq[f1] == 1) or (f2 == f1 + 1 and freq[f2] == 1):
                return True
            
            # 频率 1 只出现一次
            if (f1 == 1 and freq[f1] == 1) or (f2 == 1 and freq[f2] == 1):
                return True
        
        return False