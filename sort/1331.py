from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        r = [(arr[i], i) for i in range(n)]
        r.sort()
        ans = [0]*n
        i = 0
        rank = 1
        while i < n:
            while i+1 < n and r[i][0] == r[i+1][0]:
                ans[r[i][1]] = rank
                i += 1
            ans[r[i][1]] = rank
            rank += 1
            i += 1
        return ans

print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))