from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        idx = {}
        for i in range(len(score)):
            idx[score[i]] = i
        score.sort(reverse=True)
        metal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = [0]*len(score)
        for i in range(len(score)):
            if i <= 2:
                ans[idx[score[i]]] = metal[i]
            else:
                ans[idx[score[i]]] = str(i+1)
        return ans

print(Solution().findRelativeRanks(score = [5,4,3,2,1]))