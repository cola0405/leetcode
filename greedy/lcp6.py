from typing import List
class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = 0
        for coin in coins:
            ans += (coin+1)//2
        return ans