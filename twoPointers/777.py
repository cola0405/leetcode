class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        from collections import defaultdict
        n = len(start)
        i = 0
        d = defaultdict(str)
        d['XL'] = 'LX'
        d['RX'] = 'XR'
        while i < n:
            if start[i] != end[i]:
                if d[start[i:i+2]] != end[i:i+2]:
                    return False
                i += 1
            i += 1
        return True

print(Solution().canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))
