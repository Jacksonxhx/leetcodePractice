class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_index, n, ans = expression.find('+'), len(expression), [float(inf), expression]
        
        def evaluate(exps: str):
            return eval(exps.replace('(','*(').replace(')', ')*').strip('*'))
        
        # 到+之前
        for l in range(plus_index):
            # 从+到结尾
            for r in range(plus_index + 1, n):
                exps = f'{expression[:l]}({expression[l:plus_index]}+{expression[plus_index+1:r+1]}){expression[r+1:n]}'
                res = evaluate(exps)
                if ans[0] > res:
                    ans[0], ans[1] = res, exps
        
        return ans[1]
        