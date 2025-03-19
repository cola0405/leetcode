from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # 保存的是不相撞的行星，而不一定是同向的 -- [-2,-2,1]
        for x in asteroids:
            alive = 1   # 标记 x是否还存在
            while alive and len(stack) and x < 0 < stack[-1]:
                alive = abs(x) > abs(stack[-1])
                if abs(x) >= abs(stack[-1]):
                    stack.pop()
            if alive:
                stack.append(x)
        return stack

print(Solution().asteroidCollision([-2,-1,1,-2]))