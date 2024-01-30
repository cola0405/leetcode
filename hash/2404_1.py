from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        ans = -1
        for num in count:
            if num%2 == 0:
                if count[num] > count[ans]:
                    ans = num
                elif count[num] == count[ans]:
                    ans = min(ans, num)
        return ans

print(Solution().mostFrequentEven(nums = [0,1,2,2,4,4,1]))
