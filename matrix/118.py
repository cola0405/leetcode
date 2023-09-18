from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for layer in range(1,numRows):
            row = [1]
            for j in range(1,layer):
                row.append(ans[layer-1][j-1]+ans[layer-1][j])
            row.append(1)
            ans.append(row)
        return ans

print(Solution().generate(5))
