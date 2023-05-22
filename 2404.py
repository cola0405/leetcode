from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {num:0 for num in nums if num%2==0}
        for num in nums:
            if num%2 == 0:
                d[num] += 1

        max_times = 0
        ans = float('inf')
        for num in d:
            if d[num] > max_times:
                ans = num
                max_times = d[num]
            elif d[num] == max_times:
                ans = min(num, ans)

        if ans == float('inf'):
            return -1
        return ans

print(Solution().mostFrequentEven(nums = [0,1,2,2,4,4,1]))
