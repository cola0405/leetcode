# union find
# first-person=3, [3,5,1], [7,8,1]
# even though 3 5 7 8 are having meeting at the same time
# but neither of 7 and 8 know the secret, so they still don't know the secret

# the main problem is to mark correctly when people have meeting together
from typing import List
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        day = 0
        q = []
        meetings.sort(key=lambda x: x[2])
        parent = [i for i in range(n)]
        parent[firstPerson] = 0
        for x, y, k in meetings:
            if day != k:    # unmerge when it comes to tomorrow
                day = k
                for i in q:
                    if find(i) != 0:
                        parent[i] = i
                q = []

            if find(x) == 0 or find(y) == 0:
                parent[find(x)] = 0
                parent[find(y)] = 0
            else:
                parent[find(x)] = find(y)
            q += [x,y]
        return [i for i in range(n) if find(i) == 0]

print(Solution().findAllPeople(n = 5, meetings = [[1,4,3],[0,4,3]], firstPerson = 3))
