class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letters = [['a', a], ['b', b], ['c', c]]
        ans = ''
        while True:
            letters.sort(key=lambda item: item[1], reverse=True)
            while len(letters)>0 and letters[-1][1]==0:
                letters.pop()

            for letter in letters:  # 一次放一个才够灵活取到最大值
                if len(ans) <= 1 or ans[-1] != letter[0]\
                        or (len(ans)>=2 and ans[-2]!=letter[0]):
                    ans += letter[0]
                    letter[1] -= 1
                    break
            else:
                return ans
print(Solution().longestDiverseString(a = 1, b = 1, c = 7))


