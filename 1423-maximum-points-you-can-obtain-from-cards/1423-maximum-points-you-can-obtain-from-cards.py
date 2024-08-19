class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        keep a sliding window
        设一个最小sum的substr
        """
        n = len(cardPoints)
        m = n - k
        min_sum = s = sum(cardPoints[:m])
        for i in range(m, n):
            # iterator
            s += cardPoints[i] - cardPoints[i - m]
            min_sum = min(min_sum, s)
        
        return sum(cardPoints) - min_sum