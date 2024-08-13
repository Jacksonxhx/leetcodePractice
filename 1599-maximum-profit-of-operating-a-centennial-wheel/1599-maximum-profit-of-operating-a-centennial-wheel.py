class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        wait = 0
        max_rotations = 0
        rotations = 0
        max_profit = -1
        total_profit = 0
        total_customers = 0
        
        # 先处理所有cutsomers
        for i in range(n):
            wait += customers[i]
            rotations += 1
            
            if wait > 4:
                total_customers += 4
                wait -= 4
            else:
                total_customers += wait
                wait = 0
            
            total_profit = total_customers * boardingCost - rotations * runningCost
            
            if total_profit > max_profit:
                max_profit = total_profit
                max_rotations = rotations
        
        # 处理wait
        while wait > 0:
            rotations += 1
            
            if wait > 4:
                total_customers += 4
                wait -= 4
            else:
                total_customers += wait
                wait = 0
            
            total_profit = total_customers * boardingCost - rotations * runningCost
            
            if total_profit > max_profit:
                max_profit = total_profit
                max_rotations = rotations
        
        return max_rotations if max_profit > 0 else -1