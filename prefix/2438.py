# mod-product-prefix -- multiplicative inverse (逆元)

# congruence fit the addition, subtraction, multiplication except division
# we need to use the multiplicative inverse to deal with division
# we can't directly use pre[r+1]//pre[l]
# we need to use multiplicative inverse -- (pre[r+1] * pow(pre[l],-1,MOD)) % MOD
# a // b is equal to a multiply the multiplicative inverse of b

# pow(pre[l],-1,MOD) is to get the multiplicative inverse of b
# the multiplicative inverse of b is just the number x, which fits the equation (b*x)%m = 1
# the way to get multiplicative inverse is below:
# we can get the equation: b*x = k*m + 1
# then we can try when k=1,2,3,... until find an integer x that fits

# let's check an example:
# pre[r+1] = 24, pre[l] = 2, and the modulo is 7
# the product of interval should be (24//2)%7 = 5

# but actually the pre[r+1] will be modulo to 24%7=3
# 3//2 = 1 -- incorrect
# we should use multiplicative inverse
# (3 * multiplicative inverse of b) % 7
# the multiplicative inverse of b could be 4
# b*x = k*m + 1 --> 2*4 = 1*7 + 1
# then (3*4)%7 = 5 = (24//2)%7  --> correct

from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        cur = 1
        while n > 0:
            if n&1:
                powers.append(cur)
            n >>= 1
            cur <<= 1
        MOD = int(1e9+7)
        pre = [1]
        for num in powers:
            pre.append((pre[-1]*num) % MOD)
        ans = []
        for l,r in queries:
            ans.append((pre[r+1] * pow(pre[l],-1,MOD)) % MOD)        # 除法不满足同余
        return ans

print(Solution().productQueries(n = 919, queries = [[5,5],[4,4],[0,1],[1,5],[4,6],[6,6],[5,6],[0,3],[5,5],[5,6],[1,2],[3,5],[3,6],[5,5],[4,4],[1,1],[2,4],[4,5],[4,4],[5,6],[0,4],[3,3],[0,4],[0,5],[4,4],[5,5],[4,6],[4,5],[0,4],[6,6],[6,6],[6,6],[2,2],[0,5],[1,4],[0,3],[2,4],[5,5],[6,6],[2,2],[2,3],[5,5],[0,6],[3,3],[6,6],[4,4],[0,0],[0,2],[6,6],[6,6],[3,6],[0,4],[6,6],[2,2],[4,6]]))