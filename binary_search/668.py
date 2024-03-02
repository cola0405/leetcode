# binary search 2d sorted array

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            cnt = 0
            j = n
            for i in range(1,m+1):
                while j <= n and i*j > x:
                    j -= 1
                cnt += j
            return cnt
        low = 1
        high = m*n
        while low < high:
            mid = (low+high)//2
            if count(mid) >= k:
                high = mid
            else:
                low = mid+1
        return low

print(Solution().findKthNumber(m = 3, n = 3, k = 5))
