'''
dp + 矩阵

题目大意：给了初始位置，和二维格子的范围，每次可以上下左右移动，问总共有多少种方式可以走出界

思路：
这里很明显我们就需要对二维格子中的每一位 [i][j]建立一个状态了
但是还不够，应该还要包含当前是第几步的信息
所以有 dp[i][j][k]表示走了 k步位于 (i,j)的方案数？
那我们应该从初始位置开始 dp？总是觉得怪怪的，无法搞清楚 dp的顺序

那换一个思路，dp[i][j][k]表示位于 (i,j)还剩 k步的方案数
那此时状态又该怎么转移呢？[k-1]的状态是什么情况呢？
dp[i][j][k-1] 其实表示当前还剩 k走下一步所达到的状态，dp[i][j][k]的方案数其实就会等于四个方向[k-1]状态往回收（类似于 dfs递归）
对应到 dp，我们可以把 k的循环放到最外层，然后每次从已经更新完毕的 [k-1]状态转移过来
这样就解决了 dp顺序矛盾的问题
其次我们再来看一下初始状态的设置问题
联系 dfs递归，我们的终止条件是在 dfs出界的时候要返回 1
换句话说，我们的初始状态在边界
也就是说我们 dp往四个方向收集状态的时候，如果某个方向到界外了，则直接+1，而不用花心思构造 dp数组的初始状态
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0]*(maxMove+1) for j in range(n+1)] for i in range(m+1)]
        d = [(0,1), (0,-1), (1, 0), (-1,0)]
        for k in range(maxMove):
            for i in range(m):
                for j in range(n):
                    for dx, dy in d:
                        x, y = i+dx, j+dy
                        if 0 <= x < m and 0 <= y < n:       # 在界内，则是表示把上一个已经更新完的状态中，一步可达位置的状态都累加过来
                            dp[i][j][k+1] += dp[x][y][k]
                        else:
                            dp[i][j][k+1] += 1          # 如果 (x,y)是在结尾，则方案数+1，表示这是可以出去的一条路径
                        dp[i][j][k+1] %= MOD
        return dp[startRow][startColumn][maxMove]

print(Solution().findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0))