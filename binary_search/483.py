# find the monotonicity
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def value(base):    # calculate the value of 1's bits
            res = 0
            cur = 1
            for i in range(l):
                res += cur
                cur *= base
            return res

        ans = float('inf')
        num = int(n)
        for l in range(1,64):   # 2^18 is under 64-bits -- bits length
            low = 2
            high = num
            while low < high:       # binary search the base
                mid = (low+high)//2
                if value(mid) >= num:
                    high = mid
                else:
                    low = mid+1
            if value(low) == num:
                ans = min(ans, low)
        return str(ans)

print(Solution().smallestGoodBase("13"))


