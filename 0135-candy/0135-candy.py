class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        首先每个人最少有1根糖果
        遍历两边，如果i比i-1大，i++
        如果i比i+1大，i++
        """
        length = len(ratings)
        if length == 0:
            return 0
        
        sweets = [1] * length
        
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                sweets[i] = sweets[i - 1] + 1
        
        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                sweets[i] = max(sweets[i], sweets[i + 1] + 1)
        
        return sum(sweets)