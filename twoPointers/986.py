from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        j = 0
        ans = []
        for i in range(n1):
            l1,r1 = firstList[i]
            while j < n2:       # while for j
                l2, r2 = secondList[j]
                if r2 < l1:     # ① on the left
                    j += 1
                elif max(l1,l2) <= min(r1,r2):      # ② intersection
                    ans.append([max(l1,l2), min(r1,r2)])
                    if r2 <= r1:
                        j += 1
                    else:       # r2 > r1, cur j may still work
                        break
                else:       # ③ on the right
                    break
        return ans

print(Solution().intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
