from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        head = [1]*n
        for a,b in edges:
            head[b] = 0
        if head.count(1) != 1:
            return -1
        for team in range(n):
            if head[team] == 1:
                return team