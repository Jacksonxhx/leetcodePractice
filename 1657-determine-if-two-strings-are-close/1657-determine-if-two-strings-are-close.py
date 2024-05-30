class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        op1: 支持了所有字符串排列的顺序，意思就是只要字符数量一样，就是true
        op2: 支持了frequency的reassign，等比例配对
        所以建一个hash，只要字符都一样，数量个数都一样，就是true
        hash = {letter:{a,b,c}, frequency:{3:1, 4:2, 1:1}}
        '''
        if len(word1) != len(word2):
            return False
        
        hash1 = Counter(word1)
        hash2 = Counter(word2)
        
        hashmap1 = {'letter': set(), 'frequency': {}}
        hashmap2 = {'letter': set(), 'frequency': {}}
        
        for key, value in hash1.items():
            hashmap1['letter'].add(key)
            if value not in hashmap1['frequency']:
                hashmap1['frequency'][value] = 1
            else:
                hashmap1['frequency'][value] += 1
        
        for key, value in hash2.items():
            hashmap2['letter'].add(key)
            if value not in hashmap2['frequency']:
                hashmap2['frequency'][value] = 1
            else:
                hashmap2['frequency'][value] += 1
        
        return hashmap1['letter'] == hashmap2['letter'] and hashmap1['frequency'] == hashmap2['frequency']
        
