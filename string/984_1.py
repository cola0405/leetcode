# 测试用例推规律题

# a剩余: a - 2*(a-b) = 2*b - a
# b剩余：b - (a-b)   = 2*b - a
# 很有意思的是，贪完后居然相等了。。。

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a >= b*2:
            return 'aab'*b + 'a'*(a-b*2)
        elif b >= a*2:
            return 'bba'*a + 'b'*(b-a*2)
        elif a >= b:  # a比b多的部分，可以用来组aab
            return 'aab'*(a-b) + 'ab'*(2*b-a)
        else:
            return 'bba'*(b-a) + 'ba'*(2*a-b)

print(Solution().strWithout3a3b(2,3))


