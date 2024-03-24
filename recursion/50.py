# fast pow
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(a,b):
            if b == 0:
                return 1
            res = fast_pow(a,b//2)
            if b%2 == 0:
                return res * res    # res ** 2 will report overflow error
            else:
                return a * (res * res)

        if n >= 0:
            return fast_pow(x,n)
        else:
            return 1.0/fast_pow(x, -n)

print(Solution().myPow(2.0000000000001, -2147483648))