import collections

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        用hash存对每个字字符最后出现的位置
        然后用双指针找当前遇到的最后一位
        """
        letter_map = dict()
        for i in range(len(s)):
            letter_map[s[i]] = i
        
        res = []
        start, end = 0, 0
        for i in range(len(s)):
            end = max(end, letter_map[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        
        return res
        