class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        双指针
        """
        i, j = 0, 0
        res = []
        
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            
            # 只有这种情况有相交
            if a_start <= b_end and b_start <= a_end:
                # 开头取大，结尾取小
                res.append([max(a_start, b_start), min(a_end, b_end)])
            
            # A取完了
            if a_end <= b_end:
                i += 1              
            else:                      
                j += 1              
         
        return res