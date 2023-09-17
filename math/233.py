# 10^9 遍历肯定完蛋，说明肯定是找规律的题目
# 但如果能通过9个数位的处理就找出答案，那这道题就解决了

# 试着查看各个范围划分之间是否存在规律 -- 数字特殊，则说明研究方向对了
# ans = 0
# a = 1
# b = 10
# while a < 1e9:
#     for i in range(a,b):
#         ans += str(i).count('1')
#     print(a, b, ans)
#     a *= 10
#     b *= 10

# 根据上面的大局规律建了一张表，但是最终还是避免不了10^9量级的遍历
# table = {
#     0:0, 1:0, 10: 1, 100: 20, 1000: 300, 10000: 4000, 100000: 50000,
#     1000000: 600000, 10000000: 7000000, 100000000: 80000000,1000000000:900000000
# }


# 看指定范围内1的数量变化
# ans = 0
# for num in range(1,1000):
#     ans += str(num).count('1')
#     print(num, ans)

# 10^9遍历肯定不行，看看各数位有没有什么规律
# a = 0
# b = 0
# c = 0
#
# for num in range(1,14):
#     if num%10 == 1:
#         c += 1
#     if num//10%10 == 1:
#         b += 1
#     if num//100 == 1:
#         a += 1
# print(a,b,c)




class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        base = 1  # 表示当前是在什么位 -- 个十百千.....
        right = 1

        while n > 0:
            digit = n%10
            n //= 10
            ans += n*base

            if digit > 1:  # 当前位大于1时，该位的1出现的次数就是base
                ans += base
            elif digit == 1:  # 当前位为1时，该位的1出现的次数就是右边的数
                ans += right

            right += digit*base
            base *= 10

        return ans

print(Solution().countDigitOne(13))


