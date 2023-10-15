class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        
        #观察，罗马数字是从大到小写，当出现左边数字<右边数字时，意味着出现了像IX的情况，所以先-=左边再+=右边
        for i in range(len(s)):
            if i < len(s) - 1 and roman_int[s[i]] < roman_int[s[i + 1]]:
                res -= roman_int[s[i]]
            else:
                res += roman_int[s[i]]
        return res
            