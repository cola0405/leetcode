# 双向法

# 这题也有技巧解法
class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        L = ['RL', 'SL']
        R = ['RL', 'RS']

        # 只统计L，解决SLLL的情况
        pre = directions[0]
        for car in directions[1:]:
            pair = pre+car
            pre = car
            if pair in L:
                ans += 1
                pre = 'S'

        # 只统计R，解决RRRL的情况
        pre = directions[-1]
        for car in directions[:-1][::-1]:
            pair = car+pre
            pre = car
            if pair in R:
                ans += 1
                pre = 'S'
        return ans

print(Solution().countCollisions("LLRLRLLSLRLLSLSSSS"))
