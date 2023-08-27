# 差分 -- 区间修改

# 创造1e5长度的列表能够解决问题，但是效率太低。。。

from typing import List
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        diff = [0]*(int(1e5)+1)
        pref = [0]
        flag = [0]*(int(1e5)+1)
        for start, end, color in segments:
            diff[start] += color  # 差分 -- 区间修改
            diff[end] -= color

            # key point -- color总和相等区域是否要分段，后天的0则需要分段
            if diff[start] == 0:
                flag[start] = 1
            if diff[end] == 0:
                flag[end] = 1

        for i in range(1,len(diff)):
            pref.append(pref[-1]+diff[i])

        ans = []
        i = 1
        while i<1e5:
            if pref[i] == 0:  # 前缀和为0则表示当前区域没有涂到
                i += 1
                continue

            j = i+1
            while j<1e5 and pref[i]==pref[j] and flag[j]==0:
                j += 1
            ans.append([i, j, pref[i]])
            i = j
        return ans

print(Solution().splitPainting([[4,5,9],[8,12,5],[4,7,19],[14,15,1],[3,10,8],[17,20,18],[7,19,14],[8,16,6],[14,17,7],[11,13,3]]))






