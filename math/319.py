# 模拟法观察规律
# 1 4 9 16 ...
# 求n是第几层次 -- 平方根即可

# class Solution:
#     def bulbSwitch(self, n: int) -> int:
#         lights = [1]*n
#         if n == 1:
#             return lights
#         for step in range(1,n):
#             for j in range(step, n, step+1):
#                 lights[j] *= -1
#         return lights.count(1)
# for i in range(1,20):
#     print(i,Solution().bulbSwitch(i))

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)

print(Solution().bulbSwitch(1))



