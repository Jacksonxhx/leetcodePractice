class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        d = {}
        
        def dfs(cur):
            if tuple(cur) in d:
                return d[tuple(cur)]
            
            # 先算出来全部正价买多少钱
            val = sum(cur[i] * price[i] for i in range(len(needs)))
            
            # 遍历special offer里的offer和cost
            for *spec, cost in special:
                # 找到通过special的数量
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                # 如果最小小于0则pass
                if min(tmp) >= 0:
                    # 满足条件的话，找到min val，一直更新
                    # 从字典 d 获取 tmp 状态的最小成本，如果字典中没有该状态，则调用 dfs(tmp) 递归计算该状态的最小成本
                    val = min(val, d.get(tuple(tmp), dfs(tmp)) + cost)
                    
            # 存一对应needs的min_val    
            d[tuple(cur)] = val
            
            return val
        
        return dfs(needs)