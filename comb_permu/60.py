class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from itertools import permutations
        nums = list(range(1,n+1))
        count = 0
        for order in permutations(nums):
            count += 1
            if count == k:
                return ''.join(map(str, order))

print(Solution().getPermutation(4,9))