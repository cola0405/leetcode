class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        s = '01'
        flag = 0
        for i in range(len(target)):
            if s[flag] != target[i]:
                ans += 1
                flag ^= 1
        return ans

print(Solution().minFlips('10111'))
