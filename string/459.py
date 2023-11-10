# 数学证明题
# 这道题也可以用 KMP算法完成

# 拼接ss同时去掉首尾，然后再分为 "前" 和 "后" 两部分
# 如果 s 仍然存在于 ss 中
# 则 s 必定是在 "前" 和 "后"的交接处
# 把交接处的 s 分为 a 和 b
# 必定有 a = n*b 或者 b = n*a
# 无论是那种情况，都说明 s 必定可以由字串重复而来
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]