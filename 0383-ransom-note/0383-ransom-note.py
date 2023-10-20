class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_dict = dict()
        #记录所有字符出现了几次
        for char in ransomNote:
            if char in my_dict.keys():
                my_dict[char] += 1
            else:
                my_dict[char] = 1
            
        for char in magazine:
            if char in my_dict.keys():
                my_dict[char] -= 1
            
        for value in my_dict.values():
            if value != 0 and value > 0: return False
        
        return True
        