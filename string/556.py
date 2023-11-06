# 借助优先级队列，从右往左找下一个更大元素
# 从而使得重新排列的数字更大
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        import heapq
        digits = list(str(n))
        if len(digits) == 1:
            return -1

        pq = []
        # 然后往前找时，只要有比digit[i]大的，那就换
        min_digit = -1
        for i in range(len(digits))[::-1]:
            for j in range(len(pq)):
                if pq[j][0] > digits[i]:
                    nxt = pq[j][1]  # 下一个更大元素的下标
                    digits[i],digits[nxt] = digits[nxt], digits[i]
                    num = int(''.join(digits[:i+1] + sorted(digits[i+1:])))
                    return num if n < num <= 2 ** 31 - 1 else -1
            heapq.heappush(pq, (digits[i],i))
        return -1

print(Solution().nextGreaterElement(12443322))
