'''
二分 + 后缀

题目大意：
可以任意选择两个区间，然后求最大收益

思路：
直接暴力不行得优化
针对每个时刻的 dp也不可取，因为其取值范围是 10^9
那就还得想优化的方法，这里抓住题目只取两个区间
如果已经选定一个区间 i，那么我们要干的事情就是取不重叠区间里面收益最大的
那已经选定一个区间之后，我如何知道哪些区间是不重叠的呢？
排序 + 二分，找 start比区间 i 的 end大的区间 j，其往右的区间都是与区间 i不重叠
再构造一个后缀数组 mx保存 i往右的最大收益
那最大收益就是 events[i][2] + mx[j] 的最大值
'''


from typing import List
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        import bisect
        n = len(events)
        events.sort()                   # 按照 start排序
        mx = [0]*n
        max_val = 0
        for i in range(n)[::-1]:        # 构造后缀数组
            max_val = max(max_val, events[i][2])
            mx[i] = max_val

        ans = 0
        for i in range(n):
            ans = max(ans, events[i][2])
            end = events[i][1]

            # 二分查找 i右边第一个与区间 i不重叠的区间 j
            # 这里要注意 end+1, 因为题目要求区间端点不能重叠
            j = bisect.bisect_left(events, [end+1], i, n)
            if j < n:           # 有可能右边没有区间 j了
                ans = max(ans, events[i][2] + mx[j])
        return ans

print(Solution().maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))
