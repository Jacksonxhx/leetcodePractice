class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        use prefix and suffix
        """
        n = len(customers)
        # prefix[i]就是[0-(i-1)]之间的
        prefix, suffix = [0] * (n + 1), [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + (1 if customers[i - 1] == 'N' else 0)
        
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + (1 if customers[i] == 'Y' else 0)
        
        res = float('inf')
        best_time = 0
        for i in range(n + 1):
            penalty = prefix[i] + suffix[i]
            if penalty < res:
                res = penalty
                best_time = i

        return best_time