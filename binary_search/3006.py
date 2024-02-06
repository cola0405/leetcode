# binary search is used for search element
from typing import List
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_inx = []
        b_inx = []
        n = len(s)
        for i in range(n):
            if a == s[i:i+len(a)]:
                a_inx.append(i)
            if b == s[i:i+len(b)]:
                b_inx.append(i)
        if len(b_inx) == 0:
            return []
        ans = []
        for i in a_inx:
            left = max(0, i-k)
            low = 0
            high = len(b_inx)-1
            while low < high:
                mid = (low+high)//2
                if b_inx[mid] >= left:
                    high = mid
                else:
                    low = mid+1
            if b_inx[low] in b_inx and i-k <= b_inx[low] <= i+k:
                ans.append(i)
        return ans

