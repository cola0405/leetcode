# bfs + the shortest path
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        already = {tuple(entrance)}
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q1 = [tuple(entrance)]
        q2 = []
        ans = 0
        while q1:
            for inx in range(len(q1)):
                i,j = q1[inx]
                for k in range(4):
                    x,y = i+d[k][0],j+d[k][1]
                    if x<0 or x>=m or y<0 or y>=n:
                        if [i,j] != entrance:
                            return ans
                    elif maze[x][y] == '.' and (x,y) not in already:
                        q2.append((x,y))
                        already.add((x,y))
            q1 = q2
            q2 = []
            ans += 1
        return -1

print(Solution().nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))
