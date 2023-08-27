# 有dp思想的贪心
# 单纯每次选最远处肯定不行
# 可能错过一些可达更远的点
# 假设每次最远可达点为end1, end2, ...
# 那直接贪心会导致的唯一的问题就是
# 可能end1和end2之前存在一个点可以让end3更远...

# 但是！dp思想的贪心却可以解决这个问题！
# max_far -- 表示[end1, end2]之间可达的最远处
# 每次检查完[end1, end2]之间的各起跳点，取max_far作为下一个end
# 也就不存在错过的问题了

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        max_far = 0
        ans = 0
        for i in range(len(nums)-1):
            max_far = max(i+nums[i], max_far)
            if i == end:
                end = max_far
                ans += 1
        return ans


print(Solution().jump([2,3,1,1,4]))