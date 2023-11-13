from typing import List
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a%b)
        ans = []
        for i in range(1,n+1):
            for j in range(1,i):
                if gcd(i,j) == 1:
                    ans.append(str(j)+'/'+str(i))
        return ans

print(Solution().simplifiedFractions(3))