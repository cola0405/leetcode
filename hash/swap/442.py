# "其中nums的所有整数都在范围[1,n]内"
# 明说原地swap了。。



from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i] == nums[nums[i]-1]:
                ans.append(nums[i])
            else:
                j = nums[i]-1
                nums[i],nums[j] == nums[j],nums[i]
                