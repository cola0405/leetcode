# 枚举
# 假设反转i左边和i右边的01，达到递增的效果
# 取其中的最小反转次数

# 前缀和优化求01的次数

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        left = [0]*n   # left[i] 表示[0,i-1]之间有多少个1
        right = [0]*n  # right[i] 表示[i+1, n-1]之间有多少个0

        for i in range(1,n):
            left[i] = left[i-1]
            right[-i-1] = right[-i]

            if s[i-1] == '1':
                left[i] += 1
            if s[-i] == '0':
                right[-i-1] += 1

        ans = float('inf')
        for i in range(n):
            ans = min(ans, left[i]+right[i])
        return ans

print(Solution().minFlipsMonoIncr("010110"))