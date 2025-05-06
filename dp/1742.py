'''
数位 dp（记忆化搜索指定区间内的数字）

题目大意：有编号为 [lowLimit, highLimit]的若干小球，然后每个小球会被放到对应编号的盒子中，对应编号恰好为小球的数位和
问哪个盒子的球最多

思路：大体思路参考 1399 这里就不赘述了，下面主要阐述这道题特殊的处理
这里求 [lowLimit, highLimit]区间的数位和统计，没办法直接用前缀的减处理，此时我们就直面问题了，如何记忆化搜索指定区间内的数字
def dfs(i, s, low_same, high_same) 我们在这里就需要 2个标志位了，low_same是用来确保搜索的数字要大于等于 lowLimit
但是还有一些问题要解决
1.lowLimit的长度可能与 highLimit不一致，递归的终止条件要如何设置呢？
这里的解决方法是，在 lowLimit前面填充 0，使得 lowLimit的长度与 highLimit对齐
2.枚举当前位数字 d的取值范围应该是怎么样的呢？
我们可以通过 high_same拿到上界
那 low_same则可以帮我们拿到下界，也就是 d至少为 ..



'''

from functools import cache
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        from collections import defaultdict
        low = list(map(int, str(lowLimit)))
        high = list(map(int, str(highLimit)))
        low = [0]*(len(high)-len(low)) + low        # 在 low前面填充 0

        @cache
        def dfs(i, s, low_same, high_same):
            if i == len(high): return {s:1}
            l = low[i] if low_same else 0           # 确定当前数字 d的下界
            h = high[i] if high_same else 9         # 上界
            res = defaultdict(int)
            for d in range(l, h+1):
                cnt1 = dfs(i+1, s+d, low_same and d == l, high_same and d == h)
                for x in cnt1:
                    res[x] += cnt1[x]
            return res

        cnt = dfs(0,0,True,True)
        return max(cnt.values())

print(Solution().countBalls(lowLimit = 5, highLimit = 15))