# 往前挪的过程中可能之前的max自然而然流失。。
# dp[i]表示以i结尾，k范围内最大值 。。 没有意义 二维dp又超时 88
# 那就是用stack去模拟每一次值的流失
# 利用最大堆？可以啊，你小子... 删除操作伤不起

# 题解使用单调队列
# 然后注意，保存的不是值，而是下表
# 这样才能检查该值是否已流失

from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        mono_queue = deque()  # store indexes q[0] is the index of cur max value
        ans = [0]*(len(nums)-k+1)
        for i in range(len(nums)):
            # update mono queue
            while len(mono_queue)>0 and nums[mono_queue[-1]] < nums[i]:
                mono_queue.pop()
            mono_queue.append(i)

            # check whether out of date
            while len(mono_queue)>0 and mono_queue[0] <= i-k:
                mono_queue.popleft()

            if i>=k-1:
                ans[i-k+1] = nums[mono_queue[0]]
        return ans



print(Solution().maxSlidingWindow(nums = [1,-1], k = 1))

