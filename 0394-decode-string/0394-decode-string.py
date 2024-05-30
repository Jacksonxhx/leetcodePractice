class Solution:
    def decodeString(self, s: str) -> str:
        '''
        用stack去做
        '''
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            # 当是数的时候
            if char.isdigit():
                # handle numver bigger than 0-9
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append(current_string)
                stack.append(current_num)
                # 准备加入新的s
                current_string = ""
                # 更新num
                current_num = 0
            elif char == ']':
                num = stack.pop()
                prev_string = stack.pop()
                current_string = prev_string + num * current_string
            else:
                # 直接改变current_string地址的内容，所以stack也跟着更新
                current_string += char
        
        return current_string