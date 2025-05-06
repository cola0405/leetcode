'''
记忆化搜索

递归模拟
有时记忆化搜索比设计 dp要简单得多，前提是这里数据量不大只有 1000 剪枝之后轻轻松松
'''

from functools import cache
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        @cache
        def f(pos, step):
            if abs(pos-endPos) > step: return 0     # 剪枝操作
            if step == 0: return pos == endPos
            return (f(pos+1, step-1) + f(pos-1, step-1)) % (10 ** 9 + 7)        # 往左或者往右
        return f(startPos, k)