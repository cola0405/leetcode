from typing import List
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import Counter
        cnt = Counter(nums)
        ans = []
        for a in nums:
            b = target - a
            if a == b:
                ans += [[a,b]] * (cnt[a]//2)
                cnt[a] = cnt[a]%2
            else:
                amount = min(cnt[a], cnt[b])
                ans += [[a,b]]*amount
                cnt[a] -= amount
                cnt[b] -= amount
        return ans