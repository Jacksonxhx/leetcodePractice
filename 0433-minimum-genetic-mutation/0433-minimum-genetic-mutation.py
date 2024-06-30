from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        用bfs遍历所有组合，找到最短路
        """
        # 先check endgame
        if endGene not in bank:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = set([startGene])
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            # base case
            if current_gene == endGene:
                return mutations
            
            for i in range(len(current_gene)):
                # current_gene的每一位做ACGT的mutation
                for gene in 'ACGT':
                    
                    # 不需要mutation
                    if current_gene[i] == gene:
                        continue
                    
                    # 剩下的case
                    mutated_gene = current_gene[:i] + gene + current_gene[i+1:]
                    
                    # 如果mutated_gene在bank且没有遍历过，加入queue，做bfs
                    if mutated_gene in bank and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        queue.append((mutated_gene, mutations + 1))
        
        return -1