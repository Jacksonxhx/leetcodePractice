class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 田忌赛马，用nums1的最小值和nums2的最小值比，如果比不过就放到nums2的最大值上
        nums1.sort()
        
        n = len(nums1)
        # 把nums2排序，排序index        
        ids = sorted(range(n), key=lambda i: nums2[i])
        
        ans = [0] * n
        l, r = 0, n - 1
        
        for x in nums1:
            # 如果下等马大
            if x > nums2[ids[l]]:
                ans[ids[l]] = x
                l += 1
            else:
                ans[ids[r]] = x
                r -= 1
        
        return ans