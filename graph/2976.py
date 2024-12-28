# floyd

from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def inx(c): return ord(c)-ord('a')

        n = 26
        m = len(cost)
        min_cost = [[float('inf')]*n for _ in range(n)]
        for i in range(n): min_cost[i][i] = 0
        for i in range(m):
            min_cost[inx(original[i])][inx(changed[i])] = min(cost[i], min_cost[inx(original[i])][inx(changed[i])])
        for k in range(n):      # 注意这里不用遍历所有cost，只需要看26个中转节点即可
            for i in range(n):
                for j in range(n):
                    min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])
        ans = 0
        for i in range(len(source)):
            ans += min_cost[inx(source[i])][inx(target[i])]
        return ans if ans != float('inf') else -1

print(Solution().minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]))