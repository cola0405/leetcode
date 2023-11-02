# 递归解码


class Solution:
    def decodeString(self, s: str) -> str:
        if '[' not in s:
            return s
        res = ''
        i = 0
        times = 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                times = times*10 + int(s[i])
            elif s[i] == '[':
                stack = []
                j = i
                while j < len(s):
                    if s[j] == '[':
                        stack.append('[')
                    elif s[j] == ']':
                        stack.pop()
                    if len(stack) == 0:
                        break
                    j += 1

                seg = self.decodeString(s[i+1: j])
                res += seg*times
                times = 0
                i = j

            else:  # 不需要递归的字符直接加进去，参考用例: a2[c] -- acc
                res += s[i]
            i += 1

        return res

print(Solution().decodeString("3[a2[c]]"))
