class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        n = minutesToTest//minutesToDie
        ans = 1
        while True:
            if (2**n)**ans >= buckets:
                return ans
            ans += 1

print(Solution().poorPigs(buckets = 4, minutesToDie = 15, minutesToTest = 30))