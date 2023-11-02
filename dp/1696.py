# dp+单调队列

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
            if len(q)==k:
                q.popleft()
            while len(q)>0 and q[-1]<dp[i]:
                q.pop()
            q.append(dp[i])

        return dp[-1]