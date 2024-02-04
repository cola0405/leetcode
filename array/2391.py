from typing import List
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def get_last_inx(typ):
            for i in range(len(garbage))[::-1]:
                if typ in garbage[i]:
                    return i
            return 0
        def get_time(typ):
            total = 0
            for i in range(right_inx[typ]+1):
                total += garbage[i].count(typ)
                if i < right_inx[typ]:
                    total += travel[i]
            return total
        right_inx = {t: get_last_inx(t) for t in 'MPG'}
        return get_time('M') + get_time('P') + get_time('G')

print(Solution().garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3]))

