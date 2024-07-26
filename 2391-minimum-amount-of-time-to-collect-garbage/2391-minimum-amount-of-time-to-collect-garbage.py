class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        """
        找到每个type的highest index，依次记录路程时间
        统计所有garbage，记录collect时间
        """
        # 记录collect时间
        res = len(''.join(garbage))
        
        index_G, index_P, index_M = -1, -1, -1
        for i in range(len(garbage)):
            for ch in garbage[i]:
                if ch == 'G':
                    index_G = i
                if ch == 'P':
                    index_P = i
                if ch == 'M':
                    index_M = i
        
        index = [index_G, index_P, index_M]
        
        for i in index:
            if i <= 0:
                continue
            res += sum(travel[:i])
        
        return res
            
        