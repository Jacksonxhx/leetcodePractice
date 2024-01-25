class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        s_dict = dict()
        t_dict = dict()
        
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else: s_dict[char] = 1
        
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else: t_dict[char] = 1
                
        for key, value in s_dict.items():
            if key not in t_dict: return False
            
            if t_dict[key] != value:
                return False
        
        return True
        