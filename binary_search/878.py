# math + lcm + binary search
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        import math
        lcm = math.lcm(a,b)     # largest common multiple
        low = 0
        high = a*n      # nth number must fall in the range
        while low < high:
            mid = (low+high)//2
            if mid//a + mid//b - mid//lcm >= n:     # subtract the repeat part
                high = mid
            else:
                low = mid+1
        return low%int(1e9+7)

print(Solution().nthMagicalNumber(n = 5, a = 2, b = 4))