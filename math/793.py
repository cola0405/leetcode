# the trailing 0 is formed by the 2 and 5
# the number of 0 depends on the number of 5
# 
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count(x):   # count how many "5" if offered in factorial of x
            cnt = 0
            while x:
                x //= 5     # every step=5 will offer a "5"
                cnt += x    # for the second loop, every step=25 will also offer a "5"
            return cnt      # step = 125 will offer three "5"

        low = 0
        high = 5*k
        while low < high:
            mid = (low+high)//2
            if count(mid) >= k:
                high = mid
            else:
                low = mid+1

        return 5 if count(low) == k else 0

print(Solution().preimageSizeFZF(25))