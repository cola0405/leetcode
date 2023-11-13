from typing import List
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        import math
        ans = []
        for i in range(1,n+1):
            for j in range(1,i):
                if math.gcd(i,j) == 1:
                    ans.append(str(j)+'/'+str(i))
        return ans

print(Solution().simplifiedFractions(3))