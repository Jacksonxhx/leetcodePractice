from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 从左往右一点点挪，找到对应的abc的最短substring
        n = len(s)
        i, res = 0, 0
        cnt = defaultdict(int)

        for j in range(n):
            cnt[s[j]] += 1  # 将字符加入窗口

            # 当窗口内有至少一个 'a'、'b' 和 'c' 时
            while cnt['a'] > 0 and cnt['b'] > 0 and cnt['c'] > 0:
                # 计算从当前左边界 i 到字符串末尾的所有子字符串
                res += n - j
                cnt[s[i]] -= 1  # 移动左边界，缩小窗口
                i += 1  # 缩小窗口后左边界右移

        return res
                
                
            