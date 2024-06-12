class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        使用单调递增栈找到每一位的下一位更大的地址
        '''
        ans = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            # 当stack有东西且下一位比上一位大的时候
            # 所以不是一个一个找，而是动态的找
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 上一位的位置
                index = stack.pop()
                # 在index位的时候，
                ans[index] = i - index
            stack.append(i)
            
        return ans