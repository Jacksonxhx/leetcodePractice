class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # map函数依次把digits的内容call str()函数
        num = int(''.join(map(str, digits))) + 1

        # 将结果转换为字符串后再拆分为单个数字并存入列表
        return [int(i) for i in str(num)]