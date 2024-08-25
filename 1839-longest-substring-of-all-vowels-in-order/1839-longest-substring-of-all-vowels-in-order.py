from collections import defaultdict

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        """
        sliding window, 判断后小于前，错了i == j
        """
        vowels = "aeiou"
        res = 0
        i = 0
        
        while i < len(word):
            # 找到所有的a
            if word[i] == 'a':
                j = i
                # k 是 aeiou 中的位置
                k = 0 
                
                while j < len(word) and k < 5:
                    if word[j] == vowels[k]:
                        j += 1
                    # 下一个元音
                    elif k < 4 and word[j] == vowels[k + 1]:
                        k += 1
                    else:
                        break
                
                # 如果到u
                if k == 4:
                    res = max(res, j - i)
                    
                # 不是beautiful，i走到j的位置
                i = j       
                        
            # 遇到不是a的情况 
            else:
                i += 1
                
        return res