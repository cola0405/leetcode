from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        nums = [ord(ch) for ch in s]
        diff = [nums[0]]
        for i in range(1,n):
            diff.append(nums[i] - nums[i-1])

        offset = [-1,1]
        for l,r,d in shifts:
            diff[l] += offset[d]
            if r+1<n:
                diff[r+1] -= offset[d]

        ans = []
        pre = 0
        for i in range(len(diff)):
            pre += diff[i]
            ans.append(chr(97 + (pre-97)%26))
        return ''.join(ans)

print(Solution().shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]]))

