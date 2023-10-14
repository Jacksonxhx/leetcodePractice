class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #定义一个dictionary，每个出现过的nums的值都是一个key，然后次数是value
        cnt_dict = dict()
        n = len(nums)
        
        #遍历整个nums
        for num in nums:
            if num in cnt_dict: #如果存在++
                cnt_dict[num] += 1
            else: #不存在次数=1
                cnt_dict[num] = 1
            
        for key, value in cnt_dict.items(): #遍历这个dict中的所有key和value，然后判断
            if value > (n // 2):
                return key
'''
初始化：
my_dict = dict()
my_dict = {}

删除：
del my_dict['key4']

遍历：
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

.keys()
.values()
'''