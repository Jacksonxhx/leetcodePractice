class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        '''
        xor == 0 means x == y
        '''
        res = cur = 0
        #存储了两个值，前缀异或结果cur出现的次数，前缀异或结果的索引之和
        count = {0:[1, 0]}
        # 遍历arr
        for i, a in enumerate(arr):
            # 得到xor结果
            cur ^= a
            # 得到当前cur出现的次数和前缀和
            n, total = count.get(cur, [0, 0])
            # 计算满足条件的三元组个数
            res += i * n - total
            # 更新count cur
            count[cur] = [n + 1, total + i + 1]
        return res