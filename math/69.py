class Solution:
    def mySqrt(self, x: int) -> int:
        length = x
        width = 1
        while True:
            length = (length+width)/2
            width = x/length
            if length - width < 1e-7:
                return int(length)

print(Solution().mySqrt(4))
