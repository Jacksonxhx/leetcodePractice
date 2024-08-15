class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        subset = {i: set(favoriteCompanies[i]) for i in range(len(favoriteCompanies))}

        res = []
        for i in range(len(favoriteCompanies)):
            is_subset = True
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                elif not subset[i] - subset[j]:
                    is_subset = False
                    break
            
            if is_subset:
                res.append(i)
        
        return res