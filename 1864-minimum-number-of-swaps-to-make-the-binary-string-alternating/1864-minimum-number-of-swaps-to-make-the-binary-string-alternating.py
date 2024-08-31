class Solution:
    def minSwaps(self, s: str) -> int:
        # 正确答案只有两种：
        # 1. 0开头 2. 1开头
        cnt = Counter(s)
        n = len(s)
        
        if abs(cnt['1'] - cnt['0']) > 1:
            return -1
        
        # 两种目标字符串
        res_str1 = ''
        res_str2 = ''
        for i in range(n):
            if i % 2 == 0:
                res_str1 += '0'
                res_str2 += '1'
            else:
                res_str1 += '1'
                res_str2 += '0'
        
        res1, res2 = 0, 0
        for i in range(n):
            if s[i] != res_str1[i]:
                res1 += 1
            if s[i] != res_str2[i]:
                res2 += 1
        
        # 判断字符数量是否平衡
        if cnt['1'] > cnt['0']:
            return res2 // 2  # 只能转换为以'1'开头的
        elif cnt['0'] > cnt['1']:
            return res1 // 2  # 只能转换为以'0'开头的
        else:
            return min(res1, res2) // 2  # 两种情况都能转换，取最小值