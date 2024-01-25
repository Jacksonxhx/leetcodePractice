class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        position = dict()
        used = []
        tmp = []
        for word in strs:
            sorted_word = sorted(word)
            tmp.append(''.join(sorted_word))
            
        for i in range(len(tmp)):
            if tmp[i] in used: continue
            else: used.append(tmp[i])
            for j in range(len(tmp)):                
                if tmp[i] == tmp[j]:
                    if tmp[i] in position:
                        position[tmp[i]].append(j)
                    else:
                        position[tmp[i]] = [j]
        res = []         
        for key, value in position.items():
            tmp = [strs[i] for i in value]
            res.append(tmp)
        
        return res
            
        
        