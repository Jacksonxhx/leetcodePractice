from collections import defaultdict
from typing import List

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        '''
        使用哈希表记录每个创作者的总播放量及最受欢迎的视频
        '''
        n = len(creators)
        creator_stats = defaultdict(lambda: [0, "", float("-inf")])  # 初始化为[总播放量, 最火视频ID, 最火视频播放量]
        
        for i in range(n):
            creator = creators[i]
            video_id = ids[i]
            view_count = views[i]
            
            # 更新总播放量
            creator_stats[creator][0] += view_count
            
            # 更新最受欢迎的视频ID和播放量
            if view_count > creator_stats[creator][2]:
                creator_stats[creator][1] = video_id
                creator_stats[creator][2] = view_count
            elif view_count == creator_stats[creator][2] and video_id < creator_stats[creator][1]:
                creator_stats[creator][1] = video_id
        
        # 找到总播放量最高的创作者
        max_views = max(stat[0] for stat in creator_stats.values())
        res = []
        
        for creator, stat in creator_stats.items():
            if stat[0] == max_views:
                res.append([creator, stat[1]])
        
        return res

            
            
        
            