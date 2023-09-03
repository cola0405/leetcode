# dfs二元搜索+剪枝
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(cur, left, right):
            if cur.count('(') < cur.count(')'):  # 括号问题的剪枝
                return
            if left == 0 and right == 0:
                ans.append(cur)
                return
            if left > 0:
                generate(cur+'(', left-1, right)
            if right > 0:
                generate(cur+')', left, right-1)

        generate('', n, n)
        return ans

print(Solution().generateParenthesis(3))