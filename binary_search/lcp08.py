from typing import List
class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        from collections import defaultdict
        n = len(requirements)
        rq = [[],[],[]]
        inx = [defaultdict(list),defaultdict(list),defaultdict(list)]
        for i in range(n):
            rq[0].append(requirements[i][0])
            rq[1].append(requirements[i][1])
            rq[2].append(requirements[i][2])
        for i in range(3):  # {att: {require: [0,1,2]}}
            for j in range(n):
                inx[i][rq[i][j]].append(j)     # the requirement coule be repeated
        rq[0].sort()
        rq[1].sort()
        rq[2].sort()

        # first[i] record the day that reach the requirement for requirement[i]
        first = [[float('inf'),float('inf'),float('inf')] for y in range(n)]
        att = [0,0,0]
        p = [0,0,0]     # the pointer for every rq
        for i in range(len(increase)):
            c,r,h = increase[i]
            att[0] += c
            att[1] += r
            att[2] += h

            for j in range(3):
                while p[j] < n and rq[j][p[j]] < att[j]:
                    for index in inx[j][rq[j][p[j]]]:
                        first[index][j] = min(first[index][j],i)
                    p[j] += 1
        ans = []
        for i in range(n):
            day = min(first[i])
            if day != float('inf'):
                ans.append(day)
            else:
                ans.append(-1)
        return ans

print(Solution().getTriggerTime(increase = [[2,8,4],[2,5,0],[10,9,8]],requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]))




