from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        from collections import deque
        n = len(nums)
        q = deque([nums[0]])
        dp = [float('-inf')]*n
        for i in range(1, n):
            top = q[0]
            dp[i] = top+nums[i]
            if len(q) == k:
                q.popleft()
            while len(q)>0 and q[-1] < dp[i]:
                q.pop()
            # 要记录队首的进入时间，到时间也要清出去
            q.append(dp[i])

        return dp[-1]
print(Solution().maxResult(nums = [1,-5,-3,-7,3], k = 3))