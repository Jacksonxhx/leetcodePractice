class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        
        node_count = 1
        level = 1
        
        # 找到label在第几层
        while label >= node_count*2:
            node_count *= 2
            level += 1
        
        # 从label到root枚举
        while label != 0:
            res.append(label)
            # 因为max就是2的level次方-1，min就是2的level-1次方
            level_max = 2**(level) - 1
            level_min = 2**(level-1)
            # 找到下一层，parent在/2的地方
            label = int((level_max + level_min - label)/2)
            level -= 1
            
        # 翻转
        return res[::-1]