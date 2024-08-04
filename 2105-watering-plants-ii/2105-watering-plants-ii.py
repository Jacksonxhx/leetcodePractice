class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        if len(plants) < 2:
            return 0

        i, j = 0, len(plants) - 1
        res = 0
        waterA, waterB = capacityA, capacityB
        
        while i <= j:
            if i == j: 
                if max(waterA, waterB) < plants[i]:
                    res += 1
                break

            if waterA < plants[i]:
                res += 1
                waterA = capacityA
            waterA -= plants[i]
            i += 1

            if waterB < plants[j]:
                res += 1
                waterB = capacityB
            waterB -= plants[j]
            j -= 1

        return res