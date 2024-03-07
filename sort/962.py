from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]
        arr.sort()
        low = float('inf')
        ans = 0
        for i in range(n):      # get maximum gap
            ans = max(ans, arr[i][1] - low)
            low = min(low, arr[i][1])
        return ans

print(Solution().maxWidthRamp([6,0,8,2,1,5]))