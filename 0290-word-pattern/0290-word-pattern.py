class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_array = s.split()
        
        if len(pattern) != len(s_array): return False
        
        p_s_dict = dict()
        s_p_dict = dict()
        
        test = zip(pattern, s_array)
        for char_p, word_s in test:
            if char_p in p_s_dict:
                if p_s_dict[char_p] != word_s:
                    return False
            
            else:
                p_s_dict[char_p] = word_s
                
            if word_s in s_p_dict:
                if s_p_dict[word_s] != char_p:
                    return False
            
            else:
                s_p_dict[word_s] = char_p
                
        return True