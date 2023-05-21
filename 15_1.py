from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort + while to wipe repeat elements
        # 用升序来剪枝
        nums.sort()
        ans = []
        for k in range(len(nums)-2):
            # avoid repeat
            if len(ans)>0 and nums[k] == nums[k-1]:
                continue

            if nums[k] > 0:
                break
            i = k+1
            j = len(nums)-1

            while i < j:
                s = nums[k]+nums[i]+nums[j]
                if s<0:
                    i += 1
                    while i<j and nums[i] == nums[i-1]:
                        i += 1
                elif s>0:
                    j -= 1
                    while i<j and nums[j] == nums[j+1]:
                        j -= 1
                else:
                    ans.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while i<j and nums[i] == nums[i-1]:
                        i += 1
                    while i<j and nums[j] == nums[j+1]:
                        j -= 1
        return ans

print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))