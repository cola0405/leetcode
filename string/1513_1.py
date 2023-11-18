# 在递归的过程中其实不难发现，次数统计是有规律的
# 11   --- 3  = 2+1
# 111  --- 6  = 3+2+1
# 1111 --- 10 = 4+3+2+1


class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == '1':
                j += 1
            n = j-i
            ans += (1+n)*n // 2
            i = j+1
        return int(ans % (1e9+7))  # 题目要求取模

print(Solution().numSub("111"))
