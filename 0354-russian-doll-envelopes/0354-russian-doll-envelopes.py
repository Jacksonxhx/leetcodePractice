class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        # 固定第一位，如果第一位一样第二位按照降序排
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # dp数组记录了每一个元素代表一个当前最长递增子序列的末尾元素
        dp = []
        
        # 在 dp 数组中找到第一个大于或等于当前信封高度的位置
        def binary_search(target):
            l, r = 0, len(dp) - 1
            while l <= r:
                mid = (l + r) // 2
                if dp[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        for w, h in envelopes:
            # 获取index
            index = binary_search(h)
            # 如果index是在dp里的，需要更新这个index位置的最大值
            if index < len(dp):
                dp[index] = h
            # 不然的话append在末尾
            else:
                dp.append(h)

        
        return len(dp)