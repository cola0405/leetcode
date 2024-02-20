class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        ans = min(children, money//7)
        remain = money - ans*7
        if (ans == children and remain != 0) or (ans == children-1 and remain == 3):
            ans -= 1
        return ans

print(Solution().distMoney(money = 23, children = 2))