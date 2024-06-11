class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        对于每个spell，找到最小的能成功的potion index，用二分
        判断条件是乘积大于success
        '''
        potions.sort()
        res = []

        for spell in spells:
            l, r = 0, len(potions)
            while l < r:
                mid = (l + r) // 2
                if spell * potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1
            
            # Number of successful pairs for this spell
            res.append(len(potions) - l)
        
        return res
