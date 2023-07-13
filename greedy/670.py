# 10000 只有4个数字
# 时间复杂度 O(log n)
# 8选2枚举 O(log^2 n)
# 总时间复杂度: O(log^3 n)

# 什么概念呢？
# 100000000 - 取log后为8
# 8^3 = 512


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(map(int, str(num)))
        n = len(nums)
        ans = num
        for i in range(n):
            for j in range(i+1,n):
                nums[i], nums[j] = nums[j], nums[i]
                cur = int(''.join(map(str, nums)))
                ans = max(cur, ans)
                nums[i], nums[j] = nums[j], nums[i]
        return ans

print(Solution().maximumSwap(9973))




