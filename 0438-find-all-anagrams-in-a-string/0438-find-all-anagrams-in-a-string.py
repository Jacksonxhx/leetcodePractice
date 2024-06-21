class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        滑动窗口做，固定长度len(p)
        用hash存p里的字数，然后遍历s滑动窗口统计
        """
        # 构建p hash存判断标准
        need = collections.defaultdict(int)
        for ch in p:
            need[ch] += 1

        window = collections.defaultdict(int)
        window_size = len(p)
        res = []
        left, right = 0, 0
        valid = 0
        
        while right < len(s):
            # 当right在need中
            if s[right] in need:
                # window记录
                window[s[right]] += 1
                # 如果一个其中一个字符一样了 valid++
                if window[s[right]] == need[s[right]]:
                    valid += 1
            
            # 当长度一样后
            if right - left + 1 >= window_size:
                # 如果遇到答案
                if valid == len(need):
                    res.append(left)
                # 处理删除
                if s[left] in need:
                    if window[s[left]] == need[s[left]]:
                        valid -= 1
                    window[s[left]] -= 1
                left += 1
            right += 1
        return res
        
        
        
        