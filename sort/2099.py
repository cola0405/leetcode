from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr = [(nums[i],i) for i in range(n)]
        arr.sort(reverse=True)
        ans = arr[:k]
        ans.sort(key=lambda item: item[1])
        return [num for num,inx in ans]

print(Solution().maxSubsequence(nums = [-1,-2,3,4], k = 3))