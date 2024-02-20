class Solution:
    def minMaxDifference(self, num: int) -> int:
        s1 = list(str(num))
        for i in range(len(s1)):
            if s1[i] != '9':
                for j in range(i+1, len(s1)):
                    if s1[j] == s1[i]:
                        s1[j] = '9'
                s1[i] = '9'
                break
        maximum = 0
        for i in range(len(s1)):
            maximum = maximum*10 + int(s1[i])

        s2 = list(str(num))
        for i in range(1, len(s2)):
            if s2[i] == s2[0]:
                s2[i] = '0'
        s2[0] = '0'
        minimum = 0
        for i in range(len(s2)):
            minimum = minimum*10+int(s2[i])
        return maximum - minimum

print(Solution().minMaxDifference(11891))