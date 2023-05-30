from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num%2 == 0:
                d[num] = d.get(num,0)+1

        # find the max times
        max_times = 0
        ans = float('inf')
        for num in d:
            if d[num] > max_times:
                ans = num
                max_times = d[num]
            elif d[num] == max_times:
                ans = min(num, ans)

        # end
        if ans == float('inf'):
            return -1
        return ans

print(Solution().mostFrequentEven(nums = [0,1,2,2,4,4,1]))
