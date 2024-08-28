from collections import defaultdict

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        fre_nums1 = defaultdict(int)
        fre_nums2 = defaultdict(int)
        
        for num in nums1:
            fre_nums1[num**2] += 1
        for num in nums2:
            fre_nums2[num**2] += 1
            
        res = 0
        
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                res += fre_nums2[nums1[i] * nums1[j]]
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                res += fre_nums1[nums2[i] * nums2[j]]
        
        return res