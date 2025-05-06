'''
数位 dp（递归）

题目大意：
求出 [num1， num2]之间有多少数字的数位之和在 [min_sum, max_sum]之间

思路：
我们用 cal(num)计算出 [0,num1]和 [0,num2]之间总共有多少满足要求的数字，分别为 a和 b
那 (num1, num2]之间满足要求的数字则为 b-a，然后还要在额外判断一下 num1是否满足条件
（不用担心重复计算，我们会用到记忆化搜索）

设计 dfs(i, s, same) 进行记忆化搜索，表示到前 i位，数位和为 s的状态（可用于转移，可递归）
然后，same的意思是前面几位数字是否与 num2的数位一致
举个例子：如果区间右端点 num2 = 314
那么我们 dfs枚举到 3_ 的时候，第二位其实不能枚举 0-9中的所有数字，而是最多取到与 nums2[1] = 1

'''


from functools import cache
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        def cal(num):           # 计算
            high = list(map(int, num))
            @cache
            def dfs(i, s, same):        # 前 i为，数位和为 s，same含义看开头注释
                if i == len(high): return s >= min_sum
                cnt = 0
                up = high[i] if same else 9     # 确保当前枚举的数字不会超过 high
                for d in range(up+1):
                    if s + d <= max_sum:        # 这里条件不能写成 min_sum <= s+d <= max_sum，不然 dfs刚开始就进不去
                        cnt += dfs(i+1, s+d, same and d == up)
                return cnt
            return dfs(0,0,True)

        good_num1 = min_sum <= sum(map(int, num1)) <= max_sum
        return (cal(num2) - cal(num1) + good_num1) % MOD

print(Solution().count(num1 = "1", num2 = "12", min_sum = 1, max_sum = 8))