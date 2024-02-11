# 全员异或
# 分组异或
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res ^= num  # 全员异或，res即为A^B的结果

        h = 1
        while res&h == 0:  # 找到A和B不相同的某一位
            h<<=1

        a = 0
        b = 0
        for num in nums:
            # 根据h来分组，即可把A和B分到不同组
            # 对于其他数字，相同的数字肯定是在同一组，那分组异或就消掉了
            # a和b最后剩下的就是所求A、B的值
            if num&h:
                a ^= num
            else:
                b ^= num
        return [a,b]

print(Solution().singleNumber([1,2,1,3,2,5]))