class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while low < high:
            mid = (low+high)//2
            if mid**2 >= num:
                high = mid
            else:
                low = mid+1
        return low**2 == num