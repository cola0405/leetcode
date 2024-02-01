from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
        pre.pop(0)
        for i in range(len(pre)):
            left = pre[i]-nums[i]
            right = pre[-1]-pre[i]
            if left == right:
                return i
        return -1

print(Solution().pivotIndex([1,7,3,6,5,6]))
