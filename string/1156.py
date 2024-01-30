from collections import deque, Counter, defaultdict
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        def repeat_letter():
            for c in record:
                if intern_count[c] == max(intern_count.values()):
                    return c

        def check_low():  # 判断低频的数量是否超过1
            for c in intern_count:
                if intern_count[c] <= 1:
                    return False
            return True

        def check_high():  # 判断高频是否之后还有
            return count[repeat_letter()] > 0

        window = deque()
        count = Counter(text)
        record = set()
        intern_count = defaultdict(int)

        ans = 0
        for ch in text:
            ans = max(ans, len(window))

            window.append(ch)
            record.add(ch)
            intern_count[ch] += 1

            while (len(record) > 2
                   or (len(record) == 2 and (check_low() or check_high()))):
                head = window.popleft()
                intern_count[head] -= 1
                if intern_count[head] == 0:
                    record.remove(head)

            count[ch] -= 1
        return ans

print(Solution().maxRepOpt1("ababa"))

