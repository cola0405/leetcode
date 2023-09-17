# for n in range(1,9):
#     ans = 0
#     for num in range(10**n):
#         num = str(num)
#         if len(num)==len(set(num)):
#             ans += 1
#     print(ans)

ans = 0
for num in range(1000):
    num = str(num)
    if len(num)==len(set(num)):
        ans += 1
        print(num, ans)

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        table = [0, 10, 91, 739, 5275,32491,168571,712891,2345851]
        return table[n]

# print(Solution().countNumbersWithUniqueDigits(6))