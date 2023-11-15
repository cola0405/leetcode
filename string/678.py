# stack 记录 index
# "(" 左边的 * 是无效的，所以不能简单通过数量关系来检查有效性
# 要根据 stack 里记录的 index 来检查

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1 = []
        stack2 = []
        for i in range(len(s)):
            if s[i] == "(":
                stack1.append(i)
            elif s[i] == '*':
                stack2.append(i)
            else:
                if len(stack1) > 0:  # 贪心，有左括号就先用
                    stack1.pop()
                elif len(stack2) > 0:
                    stack2.pop()
                else:
                    return False

        if len(stack1) > len(stack2):
            return False

        # 根据 index 检查有效性
        j = len(stack2)-1
        for i in range(len(stack1))[::-1]:
            if stack1[i] > stack2[j]:
                return False
            j -= 1
        return True


print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
