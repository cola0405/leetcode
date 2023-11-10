# 滑动窗口
# 核心：答案肯定在滑动窗口中
# 有点像贪心


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        n = len(s)
        count = defaultdict(int)
        ans = 0
        total = 0

        for i in range(n):
            count[s[i]] += 1
            total += 1

            cost = total - max(count.values())  # max_count 就是当前目标字符
            while cost > k:
                count[s[i-total+1]] -= 1  # 不需要保存整个窗口的状态，while pop左窗口即可
                total -= 1
                cost = total-max(count.values())  # 每次都计算cost，不害怕目标字符改变
            ans = max(ans, total)

        return ans

print(Solution().characterReplacement("ABAA", 0))
