# hash record every state

from typing import List
class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        C = {0: 0}      # the initial day record
        R = {0: 0}
        H = {0: 0}

        cur_c = cur_r = cur_h = 0
        for i in range(len(increase)):
            c,r,h = increase[i]
            for v in range(cur_c+1, cur_c+c+1):   # iterate all changes
                C[v] = i+1    # offset
            for v in range(cur_r+1, cur_r+r+1):     # cur_r is actually for yesterday
                R[v] = i+1
            for v in range(cur_h+1, cur_h+h+1):
                H[v] = i+1
            cur_c += c
            cur_r += r
            cur_h += h

        ans = []
        for rq_c, rq_r, rq_h in requirements:
            a = C.get(rq_c, 10001)
            b = R.get(rq_r, 10001)
            c = H.get(rq_h, 10001)
            day = max(a,b,c)
            ans.append(day if day < 10001 else -1)
        return ans

print(Solution().getTriggerTime(increase = [[1,1,1]], requirements = [[0,0,0]]))




