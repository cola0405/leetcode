# swap法 -- O(1)时间复杂度

# 列表中只会出现三种数字：
# ①大于列表范围的数 -- 列表要填满，则数的范围必定是[1,n]
# ②负数
# ③范围中的数

# 对于①②，直接置-1除去
# 对于③将其swap到正确的位置即可，其中要注意列表中的数可能会重复 -- 这个时候把多余的数置-1即可

# 最后检查列表中为-1的地方，就是缺失的数


from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)  # 最右边的数最大为n
        for i in range(n):
            while nums[i] != -1 and nums[i]!=i+1:
                if nums[i] > n or nums[i]<=0 or nums[i] == nums[nums[i]-1]:
                    nums[i] = -1
                else:                # 表示是范围内的数，swap放到正确的位置
                    j = nums[i]-1    # nums[i],nums[nums[i]-1] = nums[nums[i]-1],nums[i] 有语法问题
                    nums[i], nums[j] = nums[j], nums[i]

        for i in range(n):
            if nums[i] == -1:
                return i+1
        return n+1  # 可能列表中没有-1


print(Solution().firstMissingPositive([1,1,2]))
