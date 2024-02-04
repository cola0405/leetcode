# 差分+前缀和

# 10^4 可以通过数组上色法
# 但传统标记时间复杂度是O(n2) -- 区间内每个都得标，不可行
# 联想到这是区间修改 -- 差分，修改只要O(1)的时间复杂度，加上前缀和O(n)的统计，ok了

# 就是得注意题目的测试用例包括[0,0] 这种特殊的情况
# 差分没办法处理[0,0] 只能额外处理

# 有更聪明的处理方法 -- 区间贪心，详细见56_1.py



from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        diff = [0]*int(1e4+1)
        points = set()
        for start,end in intervals:  # 构造差分数组
            diff[start] += 1
            diff[end] -= 1
            if start == end:
                points.add(start)

        prefix_sum = [diff[0]]  # 构造前缀和
        for i in range(1, len(diff)):
            prefix_sum.append(prefix_sum[-1]+diff[i])

        ans = []
        i = 0
        while i<len(prefix_sum):
            if prefix_sum[i] == 0:
                i += 1
                continue

            j = i+1
            while j<len(prefix_sum) and prefix_sum[j]!=0:
                if j in points:  # 区间中的独立端点要去掉
                    points.remove(j)
                j += 1
            ans.append([i, j])

            if i in points:
                points.remove(i)
            if j in points:
                points.remove(j)

            i = j  # while iter

        for p in points:
            ans.append([p,p])
        return ans

print(Solution().merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))



