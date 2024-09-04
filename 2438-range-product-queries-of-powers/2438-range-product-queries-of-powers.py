class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # 用binary representation of n来找powers，有1就是对应的数
        binary = bin(n)[2:]
        binary = binary[::-1]
        n = len(binary)
        powers = []
        for i in range(n):
            if binary[i] == '1':
                powers.append(2**i)
        
        res = []
        for query in queries:
            start, end = query[0], query[1]
            cnt = 1
            for i in range(start, end + 1):
                cnt *= powers[i]
            res.append(cnt % (10 ** 9 + 7))
        
        return res