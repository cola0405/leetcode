# 信息论问题
# 算法核心：
# ①小猪不同的存活状态有多少种，就可以测试多少个桶（只要信息状态数量够，就能测）
# ②小猪的总状态数 = 桶处理方式总数
# 结论：x个小猪，n轮能处理 (n+1)^x 个桶

# 举一个简单的例子来理解信息论的方法：(每只小猪同时喝多桶)
# 4个桶，1轮操作，其实只要2只小猪就够了
# x——喂药，o——不操作
#     1 2 3 4
# p1  o o x x
# p2  o x o x

# 最后两只小猪的存活状态有4种:
# 00 —— 都死 ————————— 4号桶有毒
# 01 —— p1死，p2活 ——  3号桶有毒
# 10 —— p1活，p2死 ——  2号桶有毒
# 11 —— 都活 ————————— 1号桶有毒

# 每种存活状态都直接可以和唯一的毒桶对应上
# 换句话说，小猪总共有多少种存活状态，就最多可以测多少个毒桶（下面再做可行性证明）
# "2猪1轮" —— 总共4种存活状态 —— 最多处理4个桶
# 同时也可以看到 "小猪存活状态" 其实可以抽象成2进制表示
# 2头猪表示2bits = 2^2 = 4种状态 —— (1轮2猪)

# 推广一下，1轮3猪
# 那”小猪存活状态“其实相当于3bits = 2^3 = 最多处理8个桶
# 对应的实验方案：（可以自己去试所有8种方案）
# x——喂药，o——不操作
#     1 2 3 4 5 6 7 8
# p1  o o o o x x x x
# p2  o o x x o o x x
# p3  o x o x o x o x

# 这里简单提一下方案的可行性证明
# 其实往回看之前的试验方案，可以发现一个特点，每个桶的处理方式都是不同的
# 而且他们恰恰好就是3bits的组合
# 000 001 010 011 100 101 110 111
# 其实并不是巧合，而是必然
# 只有每个桶的处理方式都不同的，才能通过这种"混喝"的方式筛出唯一的毒桶
# （如果两个桶采用一样的分配方案，那最后这两桶到底哪个是毒桶是确定不了的）
# （只要信息状态数量够，就能测）

# 进一步推广，2轮2猪
# 这时”小猪存活状态“会复杂一些
# 活——1  死——0
# 一轮：00   01       10       11
# 二轮：00   01或00   10或00   00或01或10或11
# 总计：8种 —— 最多测8桶

# 对应的实验方案：
# oo —— 第1轮、第2轮都不放， ox —— 表示第1轮不放，第2轮放
#     1  2  3  4  5  6  7  8  9
# p1  oo oo oo ox ox ox xo xo xo
# p2  oo ox xo oo ox xo oo ox xo

# 这里抽象每个桶的处理方式：
# 00 —— p1不放，p2不放
# 01 —— p1不放，p2在第1轮放
# 02 —— p1不放，p2在第2轮放
# 10 —— p1在第1轮放，p2不放
# 11 —— p1在第1轮放，p2在第1轮放
# 12 —— p1在第1轮放，p2在第2轮放
# 20 —— p1在第2轮放，p2不放
# 21 —— p1在第2轮放，p2在第1轮放
# 22 —— p1在第2轮放，p2在第2轮放
# 总计：9种 —— 其实可以看作是2位3进制数 —— 3^2 = 9

# 到这就可以进行总结了，小猪的总状态数 = (n+1)^x
# n为轮数，x为小猪数

# 还有一种计算小猪状态数的方法
# 试想：在4轮操作中，1只小猪总共有几种状态？
# 注意！！不是简单的二进制形式2^4 = 16
# 因为小猪死了之后就不可能再活
# 假设: 活——1，死——0
# 0111 这种情况时不可能出现的

# 可能的情况只有：
# 1000 —— 第1轮活，第2轮死
# 1100 —— 到第3轮才死
# 1110 —— ...
# 1111 —— ...
# 0000 —— 全程没有死
# 总计:5种 = 4+1

# 得到规律：n轮有(n+1)种状态
# 如果是x只小猪的话，则总共有: (n+1)^x种状态

# 总结：x个小猪，n轮能处理 (n+1)^x 个桶

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0

        n = minutesToTest // minutesToDie
        ans = 1
        while True:
            if (n+1)**ans >= buckets:
                return ans
            ans += 1

print(Solution().poorPigs(buckets = 125, minutesToDie = 1, minutesToTest = 4))