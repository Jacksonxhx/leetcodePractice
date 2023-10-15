class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = s.lower()
        str_array = []
        for c in str:
            if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57): 
                str_array.append(c)
        i = 0
        j = len(str_array) - 1
        while i < j:
            if str_array[i] == str_array[j]:
                i += 1
                j -= 1
            else: return False
        return True