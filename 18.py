# 再三数之和的基础上，枚举前两个数即可，后面两数仍然按照双指针

from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>=1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                # 剪枝很细节
                # 第一次要放j进来，然后再jump over repeat
                # 具体结合例子理解：[1,0,-1,0,-2,2] 0
                if j>=i+2 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = len(nums)-1
                while l<r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    if s < target:
                        l += 1
                        while l<r and nums[l]==nums[l-1]:
                            l += 1
                    elif s > target:
                        r -= 1
                        while l<r and nums[r]==nums[r+1]:
                            r -= 1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

        return ans

# [-2,-1,0,0,1,2]
print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))