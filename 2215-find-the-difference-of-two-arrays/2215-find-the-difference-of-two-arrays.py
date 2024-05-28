class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        # convert to set to avoid multiple values
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        hasht = dict()
        for num in nums1:
            if num not in hasht:
                hasht[num] = 1
            else:
                hasht[num] += 1
        
        for num in nums2:
            if num not in hasht:
                hasht[num] = -1
            else:
                hasht[num] -= 1
        print(hasht)
        
        num1, num2 = [], []
        
        for key, value in hasht.items():
            if value > 0:
                num1.append(key)
            elif value < 0:
                num2.append(key)
        
        return [num1, num2]