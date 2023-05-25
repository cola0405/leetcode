class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import defaultdict
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1

        letters = [(ch,count[ch]) for ch in count]
        letters.sort(key=lambda item: item[1], reverse=True)

        ans = ''
        for letter in letters:
            ans += letter[0]*letter[1]
        return ans

print(Solution().frequencySort(s = "Aabb"))