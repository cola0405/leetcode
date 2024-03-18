# sliding window + sorted list
from typing import List
from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sl = SortedList([nums[0]])
        i = 0
        n = len(nums)
        ans = 0
        for j in range(1, n):
            sl.add(nums[j])
            while sl and abs(sl[0] - sl[-1]) > 2:
                ans += len(sl)-1        # add when pop
                sl.remove(nums[i])
                i += 1
        ans += len(sl) * (len(sl)+1) //2
        return ans

print(Solution().continuousSubarrays([5,4,2,4]))

