# 去除两边拦不住的，在剩下的车辆中，除开S，其他的必撞
class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")
        return len(directions) - directions.count("S")

print(Solution().countCollisions("LLRLRLLSLRLLSLSSSS"))
