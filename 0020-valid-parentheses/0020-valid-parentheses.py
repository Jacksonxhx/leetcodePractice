class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0] * (len(s))
        t = -1
        for strs in s:
            if strs == "(" or strs == "[" or strs == "{":
                t += 1
                stack[t] = strs
            if strs == ")":
                if stack[t] != "(": return False
                stack[t] = 0
                t -= 1
            if strs == "}":
                if stack[t] != "{": return False
                stack[t] = 0
                t -= 1
            if strs == "]":
                if stack[t] != "[": return False
                stack[t] = 0
                t -= 1
        if t != -1: return False
        return True