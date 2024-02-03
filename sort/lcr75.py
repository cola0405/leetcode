from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        inx = {arr2[i]: i for i in range(len(arr2))}
        p1 = []
        p2 = []
        for i in range(len(arr1)):
            if arr1[i] in inx:
                p1.append(arr1[i])
            else:
                p2.append(arr1[i])
        p2.sort()
        p1.sort(key=lambda num: inx[num])
        return p1+p2

