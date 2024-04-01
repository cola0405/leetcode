# stack + custom sort
from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(reverse=True, key=lambda item: (item[0], -item[1]))
        st = []
        n = len(people)
        for i in range(n):
            tmp = []
            smaller = []
            while st and st[-1][0] < people[i][0]:
                smaller.append(st.pop())
            while len(st) > people[i][1]:
                tmp.append(st.pop())
            while smaller:
                st.append(smaller.pop())
            st.append(people[i])
            while tmp:
                st.append(tmp.pop())

        return st

print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))

