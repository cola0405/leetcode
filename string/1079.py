from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        for amount in range(1, len(tiles)+1):
            for s in permutations(tiles, amount):
                ans.add(s)
        return len(ans)

print(Solution().numTilePossibilities("AAABBC"))