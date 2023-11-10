# 常规的滑动窗口

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter,defaultdict,deque

        count1 = Counter(s1)
        count2 = defaultdict(int)
        window = deque()
        done = set()

        for i in range(len(s2)):
            window.append(s2[i])
            count2[s2[i]] += 1
            if s2[i] in count1 and count2[s2[i]]>=count1[s2[i]]:
                done.add(s2[i])

            # 维护window
            if len(window) > len(s1):
                ch = window.popleft()
                count2[ch] -= 1
                if ch in done and count2[ch] < count1[ch]:
                    done.remove(ch)

            if len(done) == len(count1):  # ps: 不是len(s1)
                return True
        return False


print(Solution().checkInclusion("abcdxabcde","abcdeabcdx"))