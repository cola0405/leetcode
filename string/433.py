# bfs

from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        n = len(bank)
        # 只差一位
        def diff(a, b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count

        # bfs
        q = deque([(startGene, 0)])
        visit = [0]*n
        while q:
            top, times = q.popleft()
            if top == endGene:
                return times
            for i in range(n):
                if visit[i] == 0 and diff(top, bank[i]) == 1:
                    q.append((bank[i], times+1))
                    visit[i] = 1
        return -1

print(Solution().minMutation(startGene = "AAAAACCC", endGene = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))
