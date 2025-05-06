'''
贪心 + 双指针

题目大意：
有一个 mxn的蛋糕，要把它切成若干个 1x1的小蛋糕
给了每条切线的代价，问最小代价是多少

思路：
越晚切的线，它要重复的次数就会越多（因为蛋糕已经被切散了）
所以，不难想到贪心策略，代价越大的我们就尽早先切
我们要对两个方向的切操作进行排序，每次选其中的代价最大的来切
然后还有一个事情要明确，某个切操作要重复几次？
这其实与另外一个方向的切操作已执行的次数有关
如果另外一个方向已经切了 1次
那么当前方向就需要重复 2次
'''

from typing import List
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        ans = 0
        i = j = 0           # i表示横向切，j表示纵向切
        while i < m-1 and j < n-1:
            if horizontalCut[i] > verticalCut[j]:
                ans += horizontalCut[i] * (j+1)     # 纵向切了 j次，则横向需要重复 j+1次
                i += 1
            else:
                ans += verticalCut[j] * (i+1)
                j += 1
        while i < m-1:
            ans += horizontalCut[i] * n
            i += 1
        while j < n-1:
            ans += verticalCut[j] * m
            j += 1
        return ans

print(Solution().minimumCost(m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]))