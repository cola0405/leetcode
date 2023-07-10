# 逆向思维贪心
# 乘法收益大，我可以认为从后往前推，必是有乘法
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            if target%2 == 0:
                target //= 2
                ans += 1
            else:
                target = (target+1)//2
                ans += 2
        ans += startValue - target
        return ans

print(Solution().brokenCalc(1,
1000000000))