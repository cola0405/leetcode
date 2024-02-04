class Solution:
    def findKthNumber(self, k: int) -> int:
        digits = 0
        pre = 1
        while True:     # find the closest left endpoint
            pre += 9 * (10**digits) * (digits+1)
            if pre > k:
                pre -= 9 * (10**digits) * (digits+1)
                break
            digits += 1
        cnt = k-pre     # the offset from the closest left endpoint
        num = 10**digits + cnt // (digits+1)    # check it with the testcase
        return int(str(num)[cnt%(digits+1)])

print(Solution().findKthNumber(k = 2147483647))



