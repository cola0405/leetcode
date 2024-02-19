# gap = full - current (prefix sum) + binary search
from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
        ans = 1
        for i in range(len(nums)):
            low = 0
            high = i
            while low < high:
                mid = (low+high)//2
                if (i-mid) * nums[i] - (pre[i]-pre[mid]) <= k:      # gap = full - current
                    high = mid
                else:
                    low = mid+1
            ans = max(ans, i-low+1)
        return ans

print(Solution().maxFrequency(nums = [1,2,4], k = 5))