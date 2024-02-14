from typing import List
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b > a:
                a,b = b,a

            while b!=0:
                a,b = b,a%b
            return a

        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                x = nums[i]
                while x >= 10:
                    x //= 10
                y = nums[j]%10
                if gcd(x,y) == 1:
                    ans += 1
        return ans

print(Solution().countBeautifulPairs([31,25,72,79,74]))
