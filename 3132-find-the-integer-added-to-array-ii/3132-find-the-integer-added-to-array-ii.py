class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # 因为只能移除两个，所以前三小至少有一个保留下来
        nums1.sort()
        nums2.sort()
        # 枚举保留 nums1[2] 或者 nums1[1] 或者 nums1[0]
        # 倒着枚举是因为 nums1[i] 越大答案越小，第一个满足的就是答案
        for i in range(2, 0, -1):
            x = nums2[0] - nums1[i]
            
            j = 0
            for v in nums1[i:]:
                if nums2[j] == v + x:
                    j += 1
                    
                    if j == len(nums2):
                        return x
            
        # 因为答案一定存在，所以返回唯一剩下的可能
        return nums2[0] - nums1[0]