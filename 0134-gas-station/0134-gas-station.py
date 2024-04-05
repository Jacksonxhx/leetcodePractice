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
            # If remGas is negative, it means start from 'i' cannot reach 'i + 1'.
            # So, we need to try starting from 'i + 1', and reset remGas to 0.
            if remGas < 0:
                start = i + 1
                remGas = 0

        # After trying all starts, if totalGas is still >= 0, it means the circuit can be completed.
        # The start point found will be the correct starting position.
        # If totalGas is negative, it means it's impossible to complete the circuit.
        return start if totalGas >= 0 else -1
