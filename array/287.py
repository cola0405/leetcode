# 数组哈希
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        for _ in range(len(nums)):
            if nums[i] == nums[nums[i]-1]:
                if i != nums[i]-1:
                    return nums[i]
                else:  # 如果已经放对，则留在当前位已经没用了，要i+=1处理下一位
                    i += 1
            # 把nums[i]送到到该放的位置
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return nums[-1]

print(Solution().findDuplicate([1,1,2]))
