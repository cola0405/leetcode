# 前驱 + set chain

# set chain 需要把遍历所有数字，时间复杂度O(n2)
# 时间主要浪费在什么地方？
# 设连续数字为x,x+1,x+2,...
# 暴力枚举会同样搜索从x+1开始的序列，浪费了时间

# 那解决问题的方法就是 -- 不让程序去对x+1等浪费时间的起点进行搜索
# 我管这个处理方法叫做前驱法 -- 只搜索前驱，即当num-1不在nums中时才搜索
# 时间复杂度是是O(n)，不会重复搜索


from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            if num-1 not in s:
                count = 1
                while num+1 in s:
                    count += 1
                    num += 1
                ans = max(count, ans)
        return ans

print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))