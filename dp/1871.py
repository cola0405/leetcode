'''
线性dp + 前缀和优化

'''

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [0] * n    # 0 表示不可达，1 表示可达
        dp[0] = 1
        pre = [0,1]
        for i in range(1,n):
            # 使用前缀和快速判断offset区间内是否有可达的点，把整体时间复杂度降到O(n)，而不用双重循环
            if s[i] == '0' and i-minJump >= 0 and pre[i-minJump+1] - pre[max(0, i-maxJump)] > 0:
                dp[i] = 1
            if dp[i]: pre.append(pre[-1] + 1)
            else: pre.append(pre[-1])
        return dp[-1] == 1

print(Solution().canReach(s = "011010", minJump = 2, maxJump = 3))