# prefix + suffix

# ps: problem ask nums[k] < nums[j], not nums[j] < nums[k]
# enumerate the middle j and k
# use prefix to check how many numbers smaller than nums[k]
# use suffix to check how many numbers greater than nums[j]

# we use a list to store the prefix
# because we need to know how many number smaller than nums[k] before index-j
# only record how many numbers smaller than nums[i] before index-i is not enough
# we need to record the performance in every position
# left[i] is the prefix about how many numbers smaller than nums[i] in different position
from typing import List
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        left = []
        right = []
        for i in range(n):
            pre = [0]
            for j in range(i):
                if nums[j] < nums[i]:
                    pre.append(pre[-1]+1)
                else:
                    pre.append(pre[-1])
            left.append(pre)

        for i in range(n):
            suf = [0]*(n+1)
            for j in range(i+1,n)[::-1]:
                if nums[j] > nums[i]:
                    suf[j] = suf[j+1] + 1
                else:
                    suf[j] = suf[j+1]
            right.append(suf)

        ans = 0
        for j in range(1,n):
            for k in range(j+1,n):
                if nums[j] > nums[k]:
                    ans += left[k][j] * right[j][k]
        return ans

print(Solution().countQuadruplets([1,3,2,4,5]))