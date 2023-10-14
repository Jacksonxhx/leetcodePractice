class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #存储三个指针以及tmp数组
        k, l, r = 0, 0, 0
        nums3 =[0] * (m + n)
        
        #直接merge
        while l < m and r < n:
            if nums1[l] < nums2[r]: 
                nums3[k] = nums1[l]
                k += 1
                l += 1
            else: 
                nums3[k] = nums2[r]
                k += 1
                r += 1
        
        #处理nums1，nums2中剩下的值
        while l < m: 
            nums3[k] = nums1[l]
            k += 1
            l += 1
        while r < n: 
            nums3[k] = nums2[r]
            k += 1
            r += 1
            
        #把值赋给nums1
        for i in range(m + n):
            nums1[i] = nums3[i]
        
        
        
            
        
        