class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numDict = dict()
        res = []
        
        for num in nums1:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        
        for num in nums2:
            if num in numDict and numDict[num]!= 0:
                numDict[num] -= 1
                res.append(num)
        
        return res