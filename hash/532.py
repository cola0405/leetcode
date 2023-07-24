from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        count = Counter(nums)
        ans = 0
        for num in count:
            if (k!=0 and k+num in count) or (k==0 and count[num]>1):
                ans += 1
        return ans

print(Solution().findPairs(nums = [3, 1, 4, 1, 5], k = 2))
