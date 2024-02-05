class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n
        while low<high:
            k = (low+high)//2
            if k*(k+1) >= 2*n:
                high = k
            else:
                low = k+1
        if low*(low+1) > 2*n:
            return low-1
        return low

print(Solution().arrangeCoins(n = 5))
