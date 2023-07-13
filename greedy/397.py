# 1的二进制即00001
# 目标是把数字转换为0001
# 当n为偶数时，最低位为0，右移即可
# 当n为奇数时，最低位为1
# -1，可以转为偶数，然后右移
# +1，可以往前把连续的1变为0，然后加一位1

# 那贪心策略就是次低位为1，就选择+1，贪尽可能多的连续1
# 否则选-1

# 这里要注意一个特殊情况，n=3时，0b11 +1因为新增1的代价，反而不如-1
# 就这个情况比较特殊，代价比不上收益，特殊处理就好了

class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n%2 == 0:
                n //= 2
                ans += 1
            else:
                if n & 0b10 and n!=3:
                    n += 1
                else:
                    n -= 1
                ans += 1
        return ans

print(Solution().integerReplacement(3))