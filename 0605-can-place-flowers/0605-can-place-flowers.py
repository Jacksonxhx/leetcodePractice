class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        i = 0
        length = len(flowerbed)
        
        while i < length:
            if flowerbed[i] == 0:
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                if next_empty and prev_empty:
                    flowerbed[i] = 1
                    cnt += 1
                    if cnt >= n:
                        return True
                    i += 1
            i += 1
        
        return cnt >= n