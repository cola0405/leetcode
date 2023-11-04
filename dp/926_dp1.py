# 因为dp只涉及到dp[i-1]
# 所以可以进行滚动dp

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        end_0 = 0
        end_1 = 0
        if s[0] == '0':
            end_1 += 1
        elif s[0] == '1':
            end_0 += 1

        for i in range(1, n):
            if s[i] == '0':
                # 如果要改以1结尾，需要操作数+1，然后前一位为0和1都可以
                end_1 = min(end_0, end_1)+1
            elif s[i] == '1':
                # 如果要改以0结尾，需要操作数+1，然后前一位只能是0
                end_1 = min(end_0, end_1)
                end_0 += 1  # end_1取完再更新end_0
        return min(end_0, end_1)

print(Solution().minFlipsMonoIncr("00110"))