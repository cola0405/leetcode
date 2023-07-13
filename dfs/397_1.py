# dp状态太多想不到怎么记录
# 那就dfs

class Solution:
    def integerReplacement(self, n: int) -> int:
        def dfs(num, op):
            if num == 1:
                return op
            if num%2 == 0:
                return dfs(num//2, op+1)
            else:
                return min(dfs(num+1, op+1), dfs(num-1, op+1))

        return dfs(n, 0)

print(Solution().integerReplacement(3))