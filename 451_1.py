class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        letters = Counter(s).most_common()
        ans = ''
        for letter in letters:
            ans += letter[0]*letter[1]
        return ans

print(Solution().frequencySort(s = "Aabb"))