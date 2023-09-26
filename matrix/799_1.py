# 把情况想得太理想了
# 所有酒杯填满的速度是不一样的，中间的快些
# 会快些到下一层，所以同一时间中间的比两端的要高

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for i in range(query_row):
            next_row = [0]*(i+2)
            for j in range(len(row)):
                next_row[j] += max((row[j]-1) / 2, 0)
                next_row[j+1] += max((row[j]-1) / 2, 0)
            row = next_row
        return row[query_glass] if row[query_glass]<=1 else 1

print(Solution().champagneTower(100000009,33,17))

