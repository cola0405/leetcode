# bfs
from typing import List
from collections import deque, defaultdict
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = deque()
        q.append(id)
        already = {id}  # make sure the shortest path is exactly "level"
        for k in range(level):
            for u in range(len(q)):
                head = q.popleft()
                for friend in friends[head]:
                    if friend not in already:
                        q.append(friend)
                        already.add(friend)
        cnt = defaultdict(int)
        videos = set()
        for friend in q:
            for video in watchedVideos[friend]:
                videos.add(video)
                cnt[video] += 1
        return sorted(videos, key=lambda x: (cnt[x], x))

print(Solution().watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2))
