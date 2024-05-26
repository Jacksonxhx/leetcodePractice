class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        双指针找范围，用popleft
        '''
        i, j = 0, 0
        while j < len(chars):
            # 如果一样快指针j++
            if chars[j] == chars[i]:
                j += 1
            # 不一样的话进入删减模式
            else:
                # 解决长度只有1的情况
                if j - i == 1:
                    i += 1
                    continue
                    
                # 记录有几个
                number = str(j - i)
                # 记录到删减到哪一位
                length = len(number) + 1
                
                # 从左边开始pop多余的
                while (i + length) < j:
                    del chars[i + 1]
                    j -= 1
                
                # 改变chars
                i += 1
                k = 0
                while k < len(number):
                    chars[i] = number[k]
                    i += 1
                    k += 1
                    
        # 处理最后一组字符
        if j - i > 1:
            number = str(j - i)
            length = len(number) + 1
            
            while (i + length) < j:
                del chars[i + 1]
                j -= 1
            
            i += 1
            k = 0
            while k < len(number):
                chars[i] = number[k]
                i += 1
                k += 1

        return len(chars)