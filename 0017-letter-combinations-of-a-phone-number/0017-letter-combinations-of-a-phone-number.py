class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        res = []
        
        def backtracking(combination, index):
            # base case，达到了位数返回
            if index == len(digits):
                combinations.append(combination)
            
            # 回溯
            else:
                # 每次进一位
                digit = digits[index]
                # 处理每位数的可能搭配
                for letter in mapping[digit]:
                    backtracking(combination + letter, index + 1)
        
        combinations = list()
        backtracking('', 0)
        return combinations
            
        
        