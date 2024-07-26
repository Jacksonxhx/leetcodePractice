class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        length = len(part)
        
        for c in s:
            stack.append(c)
            if len(stack) >= length and ''.join(stack[-length:]) == part:
                for _ in range(length):
                    stack.pop()
        
        return ''.join(stack)