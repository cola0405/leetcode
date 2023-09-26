# stack filter

from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # abc 为132模式

        stack = []  # 存放b
        c = float('-inf')
        for a in nums[::-1]:
            if a < c:  # 考虑代码的先后顺序，能进入这个if说明stack内肯定有元素 -- 则有a<c<b
                return True

            b = a  # 好好思考这一步
            while len(stack) and stack[-1] < b:  # 只把比b小的数，给c, 保证b>c
                c = max(stack.pop(), c)
            stack.append(b)  # 这一步保证了stack中肯定有元素b比c大
        return False

print(Solution().find132pattern([1,0,1,-4,-3]))