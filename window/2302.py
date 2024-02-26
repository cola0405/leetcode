# sliding window + prefix
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pre = [0]
        for num in nums:    # build prefix for window
            pre.append(pre[-1]+num)
        n = len(nums)
        i = 0
        ans = 0
        for j in range(n):  # j is ready to check
            while True:
                score = (pre[j+1]-pre[i]) * (j-i+1)
                if score >= k:
                    ans += j-i      # count when pop left
                    i += 1
                else:
                    break
        ans += (n-i)*(n-i+1) // 2
        return ans

print(Solution().countSubarrays(nums = [9,5,3,8,4,7,2,7,4,5,4,9,1,4,8,10,8,10,4,7], k = 4))

