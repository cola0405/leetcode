from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        idx = list(range(len(score)))
        idx.sort(key=lambda i: score[i], reverse=True)
        metal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = [0]*len(score)
        for i in range(len(idx)):
            if i <= 2:
                ans[idx[i]] = metal[i]
            else:
                ans[idx[i]] = str(i+1)
        return ans

print(Solution().findRelativeRanks(score = [5,4,3,2,1]))