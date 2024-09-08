class Solution:
    def largestPalindromic(self, num: str) -> str:
        # 统计每个数字出现的频率
        freq = Counter(num)
        
        # 存放构成回文对称部分的数字
        res = []
        
        # 按从大到小的顺序处理出现次数为偶数的数字，形成回文的两边
        for digit in sorted(freq.keys(), reverse=True):
            if freq[digit] // 2 > 0:
                res.append(digit * (freq[digit] // 2))
        
        # 构建回文的一半部分
        left_half = ''.join(res)
        
        # 如果有奇数次出现的数字，选择最大的放在中间
        middle = ''
        for digit in sorted(freq.keys(), reverse=True):
            if freq[digit] % 2 == 1:
                middle = digit
                break
        
        # 构造回文的完整结果
        full_palindrome = left_half + middle + left_half[::-1]
        
        while full_palindrome and full_palindrome[0] == '0':
            full_palindrome = full_palindrome[1:-1]
        
        return full_palindrome if full_palindrome != '' else '0'
        
        