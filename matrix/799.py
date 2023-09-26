# 把情况想得太理想了
# 所有酒杯填满的速度是不一样的，中间的快些
# 会快些到下一层，所以同一时间中间的比两端的要高

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured >= 10000:
            return 1

        layer = 1
        while True:
            total = (layer**2+layer) // 2
            if total > poured:
                poured -= ((layer-1)**2+(layer-1)) // 2 # 用于下一层
                layer -= 1
                break
            layer += 1

        if query_row <= layer-1:
            return 1

        single = poured / (layer*2)
        if query_glass == 0 or query_glass == layer:
            return single
        else:
            return single*2

print(Solution().champagneTower(25,6,1))

