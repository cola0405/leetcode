class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            ans = int(str(x)[::-1])
        else:
            ans = -1 * int(str(x)[1:][::-1])
        return ans if -2**31 <= ans <= 2**31-1 else 0

