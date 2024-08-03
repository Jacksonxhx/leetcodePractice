class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = [True] * (n + 1)
        p = 2
        # 找到最大可能的质数，只需到p^2
        while p * p <= n:
            if is_prime[p]:
                # 标记所有倍数
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        
        # 获得primes
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        # 写进set in method O1
        prime_set = set(primes)
        
        res = []
        for i in primes:
            if i > n // 2:
                break
            if n - i in prime_set:
                res.append([i, n - i])
        
        return res