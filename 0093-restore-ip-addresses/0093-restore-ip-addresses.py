class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        回溯算法，核心在于写回溯选择元素、递归搜索、撤销选择这三个部分
        
        约束条件：只能从 index 位置开始选择，并且要符合规则要求。
        选择元素：将其添加到当前子集数组 path 中。
        递归搜索：在选择该子段值的情况下，继续递归从剩下字符中，选择下一个子段值。
        撤销选择：将该子段值从当前结果数组 path 中移除。
        """
        res = [] # 全局变量存答案
        path = [] # 当前值
        
        def backtracking(index):
            # 如果切割次数大于 4，直接返回
            if len(path) > 4:            
                return
            
             # 切割完成，将当前结果加入答案结果数组中
            if len(path) == 4 and index == len(s):
                res.append('.'.join(path))
                return
            
            # 遍历所有选项，从index开始到结尾
            for i in range(index, len(s)):
                sub = s[index: i + 1] # 枚举每个位子组成的substring
                
                # 列举边界条件
                # 如果当前值不在 0 ~ 255 之间，直接跳过
                if int(sub) > 255:
                    continue
                # 如果当前值是0但不是单个0，跳过
                if int(sub) == 0 and i != index:
                    continue
                # 如果开头是0，跳过
                if int(sub) > 0 and s[index] == '0':
                    continue
                
                # 选择元素
                path.append(sub)
                # 递归
                backtracking(i + 1)
                # 恢复现场
                path.pop()
                
        backtracking(0)
        return res
