class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def dayOfYear(year, month, day) -> int:
            res = day
            months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                months[2] = 29
            for i in range(1, month):
                res += months[i]
            return res

        def is_leap_year(year):
            return year%400==0 or (year%100!=0 and year%4==0)

        if date1 > date2:
            date1, date2 = date2, date1

        year1, month1, day1 = map(int, date1.split('-'))
        year2, month2, day2 = map(int, date2.split('-'))

        ans = 0
        # deal with year
        for year in range(year1+1, year2):
            if is_leap_year(year):
                ans += 366
            else:
                ans += 365

        count1 = dayOfYear(year1, month1, day1)
        count2 = dayOfYear(year2, month2, day2)
        if year1 == year2:
            ans += count2-count1
        else:
            if is_leap_year(year1):
                ans += 366 - count1
            else:
                ans += 365 - count1
            ans += count2
        return ans

print(Solution().daysBetweenDates("2020-01-15",
"2019-12-31"))


