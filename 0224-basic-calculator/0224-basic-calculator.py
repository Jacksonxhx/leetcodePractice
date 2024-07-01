class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        result = 0
        # 判断正负
        sign = 1
        
        for char in s:
            if char == ' ':
                continue
            elif char.isdigit():
                # 处理multiple digits case
                current_number = current_number * 10 + int(char)
            elif char == '+':
                result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':
                result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_number
                current_number = 0
                # 获取sign
                result *= stack.pop()
                # 加上（）前的result
                result += stack.pop()
            
        result += sign * current_number
        return result