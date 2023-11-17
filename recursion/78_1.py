from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur, i):
            t = tuple(cur)
            if i == len(nums):
                ans.add(tuple(cur))
                return

            if t in ans:
                return
            # 拿或不拿
            dfs(cur, i+1)
            cur.append(nums[i])
            dfs(cur, i+1)
            cur.pop()  # 回溯

        ans = set()
        dfs([], 0)
        return list(map(list, ans))

print(Solution().subsets([1,2,3]))