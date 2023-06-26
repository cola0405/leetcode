class Solution:
    def dayOfYear(self, date: str) -> int:
        year,month,day = map(int, date.split('-'))
        ans = day
        months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if year%400==0 or (year%4==0 and year%100!=0):
            months[2] = 29
        for i in range(1,month):
            ans += months[i]
        return ans

print(Solution().dayOfYear("2003-3-1"))
