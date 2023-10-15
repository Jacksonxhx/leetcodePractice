class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1: 
                res += roman_int[s[i]]
                break
            k = i + 1
            if s[i] == "I" and (s[k] == "V" or s[k] == "X"):
                if s[k] == "V": 
                    res += 4
                    i += 2
                elif s[k] == "X":
                    res += 9
                    i += 2
                continue
            elif s[i] == "X" and (s[k] == "L" or s[k] == "C"):
                if s[k] == "L": 
                    res += 40
                    i += 2
                elif s[k] == "C":
                    res += 90
                    i += 2
                continue
            elif s[i] == "C" and (s[k] == "D" or s[k] == "M"):
                if s[k] == "D": 
                    res += 400
                    i += 2
                elif s[k] == "M":
                    res += 900
                    i += 2
                continue
            res += roman_int[s[i]]
            i += 1
        return res
            