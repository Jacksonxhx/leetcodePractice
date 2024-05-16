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
            if index == len(digits):
                combinations.append(combination)
            else:
                digit = digits[index]
                for letter in mapping[digit]:
                    backtracking(combination + letter, index + 1)
        
        
        combinations = list()
        backtracking('', 0)
        return combinations
            
        
        