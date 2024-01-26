class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 可以用greedy algo，是采用低买高卖的思想，把所有低买高卖的加起来
        # 可以把这几个数都看成是点，画出图
        profit = []
        
        for i in range(len(prices) - 1):
            cur_price = prices[i]
            nxt_price = prices[i + 1]
            
            if nxt_price <= cur_price: continue
            
            profit.append(nxt_price - cur_price)
        
        return sum(profit)