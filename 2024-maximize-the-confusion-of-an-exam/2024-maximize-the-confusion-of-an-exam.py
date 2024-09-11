class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = left = 0
        cnt = defaultdict(int)

        for right, ch in enumerate(answerKey):
            cnt[ch] += 1
            # 无法维持最大的完整情况
            # 相当于是维护一个最长子序列，其各自的数量都是小于k的
            while cnt['T'] > k and cnt['F'] > k:
                # 往左移
                cnt[answerKey[left]] -= 1
                left += 1
            # 更新ans
            ans = max(ans, right - left + 1)
        
        return ans