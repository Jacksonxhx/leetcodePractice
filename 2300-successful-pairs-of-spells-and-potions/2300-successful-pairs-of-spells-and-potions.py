class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        对于每个spell，找到最小的能成功的potion index，用二分
        判断条件是乘积大于success
        '''
        potions.sort()
        res = []
        length = len(potions)
        
        for i in range(len(spells)):
            l, r = 0, length
            
            while l < r:
                mid = (l + r) // 2
                if spells[i] * potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1
            
            res.append(length - l)
        
        return res