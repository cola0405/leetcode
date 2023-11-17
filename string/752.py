# bfs 模拟转盘
# bfs 广播找最小操作次数

from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        death = set(deadends)
        already = set()  # bfs 也会有废物操作，拨来拨去

        stack = deque([(['0','0','0','0'], 0)])
        while stack:
            top, times = stack.popleft()
            s = ''.join(top)
            if s == target:
                return times

            if s in already or s in death:
                continue
            already.add(s)
            for i in range(4):
                # +1
                t = top[:]
                t[i] = str((int(top[i])+1)%10)
                stack.append((t, times+1))

                # -1
                t = top[:]
                t[i] = str((int(top[i])+10-1) % 10)
                stack.append((t, times+1))
        return -1