class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        pre_v = [0]
        pre_c = [0]
        for ch in s:
            if ch in 'aeiou':
                pre_v.append(pre_v[-1] + 1)
                pre_c.append(pre_c[-1])
            else:
                pre_c.append(pre_c[-1] + 1)
                pre_v.append(pre_v[-1])

        ans = 0
        for i in range(1,len(pre_v)):
            for j in range(i+1,len(pre_c),2):
                v_cnt = pre_v[j] - pre_v[i-1]
                c_cnt = pre_c[j] - pre_c[i-1]
                if v_cnt == c_cnt and (v_cnt*c_cnt) % k == 0:
                    ans += 1
        return ans

print(Solution().beautifulSubstrings(s = "baeyh", k = 2))
