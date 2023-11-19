# 只关心最后一位，其他位不管不顾，则使用&1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False

        one_count = 0
        while n>0:
            if n&1:
                one_count += 1
                if one_count > 1:
                    return False
            n>>=1
        return True

print(Solution().isPowerOfTwo(1))
