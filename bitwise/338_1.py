from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        def one(num):
            count = 0
            while num > 0:
                if num&1:
                    count += 1
                num >>= 1
            return count

        return [one(i) for i in range(n+1)]