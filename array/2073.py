from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = tickets[k]
        for i in range(k):
            if tickets[i]>tickets[k]:
                ans += tickets[k]
            else:
                ans += tickets[i]
        amount = tickets[k]-1  # k位顾客刚好买完后面的不再统计
        for i in range(k+1, len(tickets)):
            if tickets[i] > amount:
                ans += amount
            else:
                ans += tickets[i]
        return ans

print(Solution().timeRequiredToBuy(tickets = [2,3,2], k = 2))