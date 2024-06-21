class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        滑动窗口做，固定长度len(p)
        用hash存p里的字数，然后遍历s滑动窗口统计
        """
        # 构建list方便操作
        p_list, s_list, res = [], [], []
        length = len(p)
        for i in p:
            p_list.append(i)
            
        for i in s:
            s_list.append(i)
            
        # 统计p的字符
        p_hash = Counter(p_list)

        # 维护一个固定大小的滑动窗口
        l, r, window = 0, 0, []
        while r < len(s):
            window.append(s_list[r])
            
            if r - l + 1 >= length:
                if Counter(window) == p_hash:
                    res.append(l)
                    
                window.pop(0)
                l += 1
            r += 1
        
        return res
        
        
        
        