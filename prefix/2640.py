from typing import List
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maximum = 0
        conver = nums[::]
        for i in range(len(nums)):
            maximum = max(maximum, nums[i])
            conver[i] += maximum

        ans = [0]
        for num in conver:
            ans.append(ans[-1]+num)
        return ans[1:]

print(Solution().findPrefixScore([2,3,7,5,10]))