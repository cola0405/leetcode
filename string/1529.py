class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        digit = 0
        for i in range(len(target)):
            if str(digit) != target[i]:
                ans += 1
                digit ^= 1
        return ans

print(Solution().minFlips('10111'))
