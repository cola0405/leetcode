from typing import List
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_stack(nums, length):
            stack = []
            available = len(nums) - length
            for num in nums:
                while len(stack) > 0 and stack[-1] < num and available > 0:
                    stack.pop()
                    available -= 1

                stack.append(num)
            return stack[:length]

        ans = []
        for a in range(len(nums1)+1):  # 枚举stack1数量
            if a>k:
                break

            b = k-a
            stack1 = get_stack(nums1, a)
            stack2 = get_stack(nums2, b)

            max_num = []
            while stack1 or stack2:  # 这个过程是类字符串比较的
                bigger = stack1 if stack1 > stack2 else stack2
                max_num.append(bigger.pop(0))
            ans = max(max_num, ans)
        return ans


print(Solution().maxNumber([9,1,2,5,8,3],[3,4,6,5],5))