class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        size = len(gas)
        start = 0
        remGas = 0
        totalGas = 0

        for i in range(size):
            totalGas += gas[i] - cost[i]
            remGas += gas[i] - cost[i]
            # 如果remGas小于0，意味着走不到
            if remGas < 0:
                start = i + 1
                remGas = 0

        # 最后如果totalGas还是
        return start 
