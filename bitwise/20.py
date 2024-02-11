# 先右移再左移

# 范围内，各数位有0则置0
# 不用担心左边部分不一致，左边部分left主导即可
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left<right:  # 只要最右边数位不一致就右移抹掉 -- 不一致就置0嘛
            left >>= 1
            right >>= 1
            count += 1

        return left<<count  # 然后再左移回来

print(Solution().rangeBitwiseAnd(10,11))
