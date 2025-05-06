'''
数位 dp

题目大意：

思路：
如果 n的范围开大，常规方法就过不了了
因为涉及到数位和，所以考虑数位 dp
记忆化搜索 dfs(i,s,same) 表示前 i为，和为 s的状态
same的意思是前面几位数字是否与 num一致
举个例子：如果区间右端点 num = 314
那么我们 dfs枚举到 3_ 的时候，第二位其实不能枚举 0-9中的所有数字，而是最多取到与 num2[1] = 1
dp处理大体与 2719一致
区别在于，这里要把各个不同数位和都做一个统计
不能在 dfs中做 cnt[s]+=1
因为我们记忆化搜索的核心在于要利用已有状态，之前统计好的状态我们要直接拿过来用
然后，这里不是简单的要一个总数，而是各种不同数位和的数量
所以，我们每个状态要保存的就不是一个单纯的返回值，而是一个统计了若干数位和数量的字典
'''

from functools import cache
class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        num = list(map(int, str(n)))
        @cache
        def dfs(i,s,same):
            if i == len(num): return {s:1}      # 最终状态肯定要返回当前的和 s
            res = defaultdict(int)              # 用于保存当前 dfs(i,s,same)状态的统计
            up = num[i] if same else 9
            for d in range(up+1):
                cnt1 = dfs(i+1, s+d, same and d == num[i])      # 这里是记忆化搜索的核心，利用已有状态
                for x in cnt1:
                    res[x] += cnt1[x]
            return res

        cnt = dfs(0,0,True)
        cnt.pop(0)                 # 因为题目不考虑 0，所以要先剔除掉
        max_cnt = max(cnt.values())
        return sum(v == max_cnt for v in cnt.values())

print(Solution().countLargestGroup(2))