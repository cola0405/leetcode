# 问题转化为 —— 相同的数字必须在同一区间
# ans = 2 ^（区间数-1）

# 举一个例子：
# [3]+[1,2,1,2]+[4,4]
# 最终的方案数为4 —— 说白了就是每个加号合并不合并

# 那这道题就转而变为合并区间的一道题 —— 可以参考 56.合并区间

from typing import List
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        rev_nums = nums[::-1]
        end_inx = dict()   # 记录某数字最后一次出现的index
        for i in range(len(nums)):
            if rev_nums[i] not in end_inx:
                end_inx[rev_nums[i]] = len(nums)-1-i

        interval_cnt = 0
        i = 0
        while i < len(nums):
            interval_cnt += 1
            end = end_inx[nums[i]]
            while i < end:
                end = max(end, end_inx[nums[i]])
                i += 1
            i += 1
        ans = 1
        for i in range(interval_cnt-1):
            ans *= 2
            ans %= 1e9 + 7
        return int(ans)

print(Solution().numberOfGoodPartitions([1,2,3,4]))