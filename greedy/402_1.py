# 5496ms
# list的pop效率低，用deque相对好一些，但仍然慢
# stack的优势就体现出来了 80ms -- 也从这发现了stack对于pop操作的优化

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        from collections import deque
        nums = deque(num)
        # 一趟走完
        i = 0
        j = 1
        while j<len(nums) and k>0:
            if nums[i]>nums[j]:
                nums.remove(nums[i])
                i = max(0, i-1)
                j = max(1, j-1)
                k -= 1
            else:
                i += 1
                j += 1
        while k>0:
            nums.pop()
            k -= 1
        while len(nums)>1 and nums[0]=='0':
            nums.popleft()
        if len(nums) == 0:
            return '0'
        return ''.join(nums)

print(Solution().removeKdigits("1432219",
3))
