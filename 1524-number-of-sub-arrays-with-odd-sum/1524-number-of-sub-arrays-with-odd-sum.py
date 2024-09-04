class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # 先写一个前缀合，然后对于odd sum，找前面是even的number，就是对应的数量
        # 用一个数组记录当前i位置前有多少个even和odd
        
        # even, odd
        count = [1, 0]
        
        cur = res = 0
        
        for i in arr:
            # 判断odd even
            cur ^= i & 1
            
            # 如果当前前缀合是odd，+even，vise versa
            res += count[1 - cur]
            
            count[cur] += 1
        
        return res % (10**9 + 7)