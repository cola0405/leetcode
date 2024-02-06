# from lower-bound to (upper-bound under the target)

from typing import List
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        b.sort()
        min_diff = float('inf')
        for num in a:
            low,high = 0,len(b)-1
            while low < high:       # lower-bound above the target
                mid = (low+high)//2
                if b[mid] >= num:
                    high = mid
                else:
                    low = mid+1
            min_diff = min(min_diff, abs(num-b[low]))

            if low > 0:     # upper-bound under the target
                min_diff = min(min_diff, abs(num-b[low-1]))
        return min_diff

print(Solution().smallestDifference([-2147483648,1],[2147483647,0]))