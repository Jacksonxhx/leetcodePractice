from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        # rank[team][j] 记录的是 team 在 j-th 位置上收到的票数
        rank = defaultdict(lambda: [0] * n)
        
        # 遍历每一张投票
        for vote in votes:
            for i, team in enumerate(vote):
                rank[team][i] += 1
        
        # 排序的优先级是：先比较各自的排名票数，如果相同则按字母顺序排列
        # 对keys排序，根据rank[x]来排序，如果打平，按照x的alphabetically排序
        result = sorted(rank.keys(), key=lambda x: (rank[x], -ord(x)), reverse=True)
        
        return ''.join(result)
            