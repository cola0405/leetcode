from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = sorted([(nums[i], i)for i in range(n)])
        ans = [0]*n
        i = 0
        while i < n:
            cnt = i
            while i+1 < n and arr[i][0] == arr[i+1][0]:
                ans[arr[i][1]] = cnt
                i += 1
            ans[arr[i][1]] = cnt
            i += 1
        return ans

print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))