# 位运算+补码的掌握
# 很经典的一道题
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):  # 32个数位都过一遍
            bit = 1 << i
            count = 0
            for num in nums:
                if num & bit:
                    count += 1
            # 如果第i数位竖着框下来，1的数量不是3的倍数
            # 则说明那唯一的元素在第i位值为1
            # 这道题的坑就在于负数在计算机是按补码存储的，位运算完还要处理负数的问题
            if count%3 != 0:
                res |= bit
                if i == 31:
                    res -= 2**32

        # 由于i枚举了32位，所以符号位也会被包括在内
        # 当nums中有负数时会有问题
        # 因为python是动态类型的语言，原本应该是符号位的1，在res中会被当成是值！
        # 也就出现了莫名其妙的大值
        # input: [-2,-2,1,1,4,1,4,4,-4,-2]
        # output: 4294967292

        # 解决方法：res -= 2**32
        # 如果第32位(符号位)是1，则应该把大值转化为对应的负数
        # 又已知11...1(32位全1)对应-1，11...10对应-2
        # 根据数轴分布，可知与10...0(首位为第33位，值为2**32)做差可得对应的负数
        # 8=1000 为2**3
        return res

print(Solution().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))