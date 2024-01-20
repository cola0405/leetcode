# 子字符串、连续 -- 滑动窗口

from collections import deque
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[i])-ord(t[i])) for i in range(n)]

        ans = 0
        cur_cost = 0
        window = deque()
        for i in range(n):
            window.append(cost[i])
            cur_cost += cost[i]
            while window and cur_cost > maxCost:
                head = window.popleft()
                cur_cost -= head
            ans = max(ans, len(window))
        return ans

print(Solution().equalSubstring(s = "abc", t = "abc", maxCost = 3))