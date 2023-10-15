class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.strip().split()
        index = len(strs) - 1
        return len(strs[index])
         