from typing import List
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        k = len(indices)
        for i in range(k-1):
            for j in range(k-i-1):
                if indices[j] > indices[j+1]:
                    indices[j], indices[j+1] = indices[j+1],indices[j]
                    sources[j], sources[j+1] = sources[j+1],sources[j]
                    targets[j], targets[j+1] = targets[j+1], targets[j]

        ans = ''
        i,j = 0,0
        while i < len(s):
            if j == k or i != indices[j]:
                ans += s[i]
                i += 1
                continue

            if sources[j] == s[i:i+len(sources[j])]:
                ans += targets[j]
                i += len(sources[j])
            else:
                if not (j+1 < k and indices[j+1] == i):
                    ans += s[i]
                    i += 1
            j += 1

        return ans

print(Solution().findReplaceString("abcde" , [2,2], ["bc","cde"], ["fe","f"]))