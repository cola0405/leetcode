from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        from itertools import combinations
        ans = []
        for comb in combinations(range(1,10), k):
            if sum(comb) == n:
                ans.append(list(comb))
        return ans

print(Solution().combinationSum3(k = 3, n = 7))