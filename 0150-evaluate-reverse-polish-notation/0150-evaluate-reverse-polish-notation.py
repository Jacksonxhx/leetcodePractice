class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 构造一个stack，如果遇到数字，就往stack插入，遇到符号pop两个数进行计算重新插入栈中
        stack = [0] * (len(tokens) + 1)
        head = 0
        operator = ["+", "-", "*", "/"]
        def pop(stack, head):
            tmp = stack[head]
            stack[head] = 0
            head -= 1
            
            return stack, head, tmp
            
        for token in tokens:
            if token not in operator:
                head += 1
                stack[head] = token
            else:
                if token == "+":
                    stack, head, tmp1 = pop(stack, head)
                    stack, head, tmp2 = pop(stack, head)
                    
                    tmp3 = int(tmp1) + int(tmp2)
                    head += 1
                    stack[head] = tmp3
                
                elif token == "-":
                    stack, head, tmp1 = pop(stack, head)
                    stack, head, tmp2 = pop(stack, head)
                    
                    tmp3 = int(tmp2) - int(tmp1)
                    head += 1
                    stack[head] = tmp3
                
                elif token == "*":
                    stack, head, tmp1 = pop(stack, head)
                    stack, head, tmp2 = pop(stack, head)
                    
                    tmp3 = int(tmp2) * int(tmp1)
                    head += 1
                    stack[head] = tmp3
                
                elif token == "/":
                    stack, head, tmp1 = pop(stack, head)
                    stack, head, tmp2 = pop(stack, head)
                    
                    tmp3 = int(tmp2) / int(tmp1)
                    head += 1
                    stack[head] = tmp3
        
        return int(stack[1])
            