class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        """
        Set substring length L
        因为vowels == consonants
        所以L^2 % 4k == 0
        所以找到一个d s.t. L % d == 0
        """
        # 找d
        for d in count(1):
            if d*d % (4*k) == 0:
                k = d
                break
        
        # 做题，L % k == 0
        # 元音1，辅音-1，找前缀合为0的
        prefix = [0]
        for ch in s:
            x = 1 if ch in 'aeiou' else -1
            prefix.append(prefix[-1] + x)
        
        # 哈希表统计 pair (i%k', sum[i]) 的出现次数，这里k' = d
        res = 0
        cnt = Counter()
        for i, s in enumerate(prefix):
            p = (i % k, s)
            # 找到i左边有多少个一样的j，加到res
            res += cnt[p]
            cnt[p] += 1
        
        return res
        