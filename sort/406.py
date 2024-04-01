from typing import List
class item:
    def __init__(self,h,k):
        self.h = h
        self.k = k

    def __lt__(self, other):
        if self.h == other.h:
            return self.k < other.k
        return self.h > other.h

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        arr = sorted([item(h,k) for h,k in people])
        st = []
        n = len(arr)
        for i in range(n):
            tmp = []
            smaller = []
            while st and st[-1].h < arr[i].h:
                smaller.append(st.pop())
            while len(st) > arr[i].k:
                tmp.append(st.pop())
            while smaller:
                st.append(smaller.pop())
            st.append(arr[i])
            while tmp:
                st.append(tmp.pop())

        return [[t.h,t.k] for t in st]

print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))

