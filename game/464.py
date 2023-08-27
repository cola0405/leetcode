# 博弈 + 记忆化搜索
# 经典
# 优化版本在1

# 表现最佳，意思就是两个人都会 「在每次选择前，分析后续所有可能的结果，然后布局」
# 那么这道题就不是简单的if能够做决策的了 -- 需要搜索
# 引用象棋的概念 -- 走一步看三步，但是这里我们需要用递归直接看到底
# 下棋双方都用一套递归去搜索分析，那么双方就都是最佳策略

# 递归思路：
# 递归winner() -- 搜索当前局面下胜者是谁
# 递归思路: winner(选取一个数字后的新局面) 如果返回的仍然是当前player，则就下这一步

# 递归具体代码逻辑：
# 关注顶层递归
# 全部可选数字都都递归搜索一遍，如果其中有一个搜出来仍然是自己，则返回自己，表示自己稳赢
# 如果这若干个位置都无法胜利，则顶层递归返回对手，表示对手胜利
# 递归终止条件：total>=target -- 搜到这里就可以确定比赛结果了，
# 然后把胜利者返回到上一层

# 递归过程中需要回溯
# 单纯回溯还不够，会超时
# 需要记忆搜索 -- 局面可能会有重复，即使选取的先后顺序不一样，但是到那个局面的时间节点都是一样的！
# 所以可以以局面为key构造哈希表记录胜利者
# 要注意的就是需要在选取之前记录，不能回溯后记录 -- 待选取状态才是对应的局面


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        nums = list(range(1,maxChoosableInteger+1))
        available = [1]*len(nums)

        win = dict()
        def winner(total, player):  # 搜索当前局面一棋就奠定胜局的player
            state = tuple(available)  # 当前局面
            if state in win:
                return win[state]

            if total >= desiredTotal:
                win[state] = player*-1
                return player*-1  # 返回对手 (自己已经没机会下了)

            for i in range(len(available)):
                if available[i]:
                    available[i] = 0
                    total += nums[i]
                    if winner(total,player*-1) == player:
                        available[i] = 1  # return 前回溯
                        total -= nums[i]

                        win[tuple(available)] = player  # 回溯完再记录！待选状态才是我们需要的
                        return player

                    available[i] = 1  # 回溯
                    total -= nums[i]

            return player*-1  # 1表示先手的player1，-1表示player2

        if desiredTotal == 0:
            return True
        if sum(range(1,maxChoosableInteger+1)) < desiredTotal:
            return False
        return winner(0, 1) == 1  # 1表示先手的player1

print(Solution().canIWin(20, 152))