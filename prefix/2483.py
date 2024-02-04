# homemade-prefix

# the key is the time to close the shop
# then we can analyse the penalty before and after
# before: the shop is open, but no customer
# after: the shop is closed, but do have customers

# according the practical issue, add the extra item to prefix
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pre_y = [0]
        pre_n = [0]
        for typ in customers:
            if typ == 'Y':
                pre_y.append(pre_y[-1]+1)
                pre_n.append(pre_n[-1])
            else:
                pre_y.append(pre_y[-1])
                pre_n.append(pre_n[-1]+1)

        # it can close the shop after all logs, so we need to add an extra item
        pre_y.append(pre_y[-1])
        pre_n.append(pre_n[-1])
        n = len(customers)
        ans = 0
        min_penalty = pre_y[-1]
        for i in range(2,n+2):
            penalty = (pre_y[-1]-pre_y[i-1]) + pre_n[i-1]
            if penalty < min_penalty:
                min_penalty = penalty
                ans = i-1   # offset
        return ans

print(Solution().bestClosingTime("YN"))