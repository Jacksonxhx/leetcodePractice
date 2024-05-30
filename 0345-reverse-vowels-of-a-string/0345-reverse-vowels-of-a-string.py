class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        双指针前后一起走，找到元音停下交换
        '''
        i, j = 0, len(s) - 1
        vowels = set('aeiouAEIOU')
        s_array = list(s)
        
        while i < j:
            while i < j and s_array[i] not in vowels:
                i += 1
            
            while i < j and s_array[j] not in vowels:
                j -= 1
            
            if i < j:
                s_array[i], s_array[j] = s_array[j], s_array[i]
                i += 1
                j -= 1
        
        return "".join(s_array)