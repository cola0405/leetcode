# (a⋅b) mod m=[(a mod m)⋅(b mod m)] mod m

from typing import List
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def sp(x,y,mod):
            if y == 0:
                return 1
            x %= mod
            res = sp(x, y//2, mod)
            if y%2 == 0:
                return (res**2) % mod
            else:
                return (res**2 * x) % mod

        ans = 1
        for digit in b[::-1]:
            ans = (ans * sp(a, digit, 1337)) % 1337
            a = sp(a, 10, 1337)
        return ans

print(Solution().superPow(a = 2147483647, b = [2,0,0]))