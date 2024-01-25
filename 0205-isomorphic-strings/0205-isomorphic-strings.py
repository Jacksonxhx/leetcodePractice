class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        s_t_dict = dict()
        t_s_dict = dict()
        
        for char_s, char_t in zip(s, t):
            if char_s in s_t_dict:
                if s_t_dict[char_s] != char_t:
                    return False
            
            else:
                s_t_dict[char_s] = char_t
                
            if char_t in t_s_dict:
                if t_s_dict[char_t] != char_s:
                    return False
            
            else:
                t_s_dict[char_t] = char_s
        
        return True
        
        
        
    
        
        