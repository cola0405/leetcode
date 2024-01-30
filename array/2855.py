from typing import List
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        def is_sorted():
            for j in range(i,i+n-1):
                if nums[j%n] > nums[(j+1)%n]:
                    return False
            return True

        n = len(nums)
        nums += nums
        for i in range(n):
            if is_sorted():
                if i == 0:
                    return 0
                else:
                    return n-i
        return -1

print(Solution().minimumRightShifts([1,2]))
