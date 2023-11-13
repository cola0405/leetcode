# 贪心
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ''
        while a >= 1 and b >= 1:
            if a > b:
                ans += 'aab'
                a -= 1
            elif a < b:
                ans += 'bba'
                b -= 1
            else:
                ans += 'ab'
            a -= 1
            b -= 1

        while b > 0:
            ans += 'b'
            b -= 1
        while a > 0:
            ans += 'a'
            a -= 1
        return ans

print(Solution().strWithout3a3b(4,1))


