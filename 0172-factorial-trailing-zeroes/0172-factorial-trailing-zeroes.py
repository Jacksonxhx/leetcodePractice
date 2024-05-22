class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        method 1: recursion call一遍获取阶乘的答案然后reverse数0
            这个方法会溢出
        
        method 2：因为尾随0的多少由10决定，而10由5决定，所以直接算5的数量
        '''
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
        
#         import sys
#         sys.set_int_max_str_digits(1000000)
#         def fact(n, ans=1):
#             if n <= 1:
#                 return ans
#             return fact(n - 1, ans * n)
        
#         # 计算阶乘
#         ans = fact(n)
        
#         # 将阶乘结果转换为字符串并倒序
#         str_ans = str(ans)[::-1]
        
#         # 计算尾随零的数量
#         res = 0
#         for i in str_ans:
#             if i == '0':
#                 res += 1
#             else:
#                 break
        
#         return res