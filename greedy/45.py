# https://leetcode.cn/problems/jump-game-ii/description/

# 贪心
# 转化研究对象为：n次跳跃最远可以到的点
# 从左往右遍历过程中不断更新最远可以到的点，同时统计跳跃次数即可

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