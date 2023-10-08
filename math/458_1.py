# 这个是对(n+1)^x > N，两边取对数的公式推导 —— 取到x的最小值

# 之所以减1e-8 是因为对数有误差
# 故不推荐，还是方法一老实遍历就行，高维计算不会枚举太多的

# 可以用一下方法查看误差
# print(math.log(buckets) / math.log(n+1))


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        import math
        n = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets) / math.log(n+1) - 1e-8)

print(Solution().poorPigs(buckets = 125, minutesToDie = 1, minutesToTest = 4))