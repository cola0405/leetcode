# 由于某个字母只是有或没有
# 可以把区间状态压缩到bits中

# 0:偶数, 1:奇数
# 首先，如何记录状态：
# 每多一个字母，奇偶状态就取反一次
# 其实就是与 1 进行异或

# 然后，如何知道区间内的奇数字母的数量：
# [left, right] 分别取到两个状态: s1 和 s2
# 下面列举bit变化的所有情况：
# ① 0 -> 1, [left, right]区间内有奇数个字母
# ② 1 -> 0, [left, right]区间内有奇数个字母
# ③ 0 -> 0, [left, right]区间内有偶数个字母
# ④ 1 -> 1, [left, right]区间内有偶数个字母

# 不难发现，正好是异或运算^
# 之前用前缀和做减法来知道数量的奇偶性
# 现在只要对每个bit异或，即可知道该字母在区间内数量的奇偶性

from typing import List
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        status = [0]
        for ch in s:
            # 表明了各个字母的奇偶状态变化，0:偶数, 1:奇数
            bits = status[-1] ^ (1 << (ord(ch) - 97))
            status.append(bits)

        ans = []
        for left, right, k in queries:
            # 26 个字母都检查一遍
            s1, s2 = status[left],status[right+1]  # 闭区间
            odd, bit = 0, 1

            for i in range(26):  # 统计区间内数量为奇数的字符
                if s1&bit ^ s2&bit:
                    odd += 1
                bit <<= 1

            ans.append(odd-2*k <= 1)

        return ans


print(Solution().canMakePaliQueries("abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))


