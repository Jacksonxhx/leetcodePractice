class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #定义一个最小price和最大利润
        minprice = max(prices)
        maxprofit = 0
        
        #核心思想：
        #从左往右遍历，记录当前最小值
        #maxprofit = 每一次price-minprice的最大值
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
            
        return maxprofit