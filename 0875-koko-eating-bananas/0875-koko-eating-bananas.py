class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        首先吃香蕉的速度范围是：[1, max(piles)]，所以就是在这个区间判断
        判断条件是：能否以k的速度在h小时内吃完
        如果吃不完，证明太慢了，l = mid + 1
        吃得完，证明太快了，r = mid - 1
        '''
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if not self.canEat(piles, h, mid):
                l = mid + 1
            else:
                r = mid
        
        # 当了l == r的时候跳出
        return l
    
    def canEat(self, piles, h, speed):
        time = 0
        for pile in piles:
            time += (pile + speed - 1) // speed
        return time <= h