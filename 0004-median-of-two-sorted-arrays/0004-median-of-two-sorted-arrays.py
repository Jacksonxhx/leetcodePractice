class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        直接在nums1和nums2找
        因为median是（n1 + n2 + 1）/ 2 = k
        所以题目就是在两个有序数组中找到前 k 小的元素位置
        如果从nums1取m1个，那从nums2就取m2=k−m1个
        
        通过二分的方法，在数组nums1里找到合适的位置
        '''
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        # 中位数
        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        
        # 二分
        while left < right:
            m1 = (left + right) // 2
            m2 = k - m1
            # 比较nums1[m1]和nums2[m2 - 1]
            
            # 意味着nums1从0-(m1-1)都不是k
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1
        
        # 找到正确的m1后
        m1 = left
        m2 = k - m1
        
        # 左半边的max
        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1], float('-inf') if m2 <= 0 else nums2[m2 - 1])
        
        # 奇数的情况
        if (n1 + n2) % 2 == 1:
            return c1

        # 右半边的min
        c2 = min(float('inf') if m1 >= n1 else nums1[m1], float('inf') if m2 >= n2 else nums2[m2])
        
        # 偶数的情况
        return (c1 + c2) / 2
                