# 二分并不要求一定要有序
# 前半部分不行，后半部分行，lower bound场景下也可以使用二分
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        p = [0]
        for num in nums:
            p.append(p[-1]+num)
        ans = float('inf')
        for i in range(1,n+1):
            low = i
            high = n
            while low<high:  # lower bound
                mid = (low+high)//2
                s = p[mid]-p[i-1]
                if s >= target:
                    high = mid
                else:
                    low = mid+1
            if p[low]-p[i-1] >= target:
                ans = min(low-i+1, ans)

        return ans if ans!=float('inf') else 0