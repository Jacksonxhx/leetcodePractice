class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        单调栈做，如果遇到比stack[-1]大的，pop，加入新的
        如果stack里有，比当前小，继续pop
        """
        length = len(temperatures)
        
        # 存当前数的index
        stack = []
        res = [0] * length
        
        for i in range(length):
            # 当stack有且当前数大于stack里最新的数的时候
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 得到最新的stack的数位置
                index = stack.pop()
                # 在res中的当前位置求距离
                # 因为当前i位是第一个比index位大的，所以是i-index
                res[index] = i - index
            stack.append(i)
            
        return res