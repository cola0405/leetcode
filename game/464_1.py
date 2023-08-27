# 01 可以用位操作优化空间
# 节约空间的同时，也少了很多申请内存的操作，也提高了时间效率

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        nums = list(range(1,maxChoosableInteger+1))
        state = 0  # bit=0表示可用，bit=1表示不可用

        win = dict()
        def winner(total, player):
            nonlocal state
            if state in win:
                return win[state]

            if total >= desiredTotal:
                win[state] = player*-1
                return player*-1

            cur = 1  # 用于修改某bit
            for i in range(maxChoosableInteger):
                if not state & cur:  # 独看一位用&
                    state |= cur
                    total += nums[i]
                    if winner(total,player*-1) == player:
                        state ^= cur  # return 前回溯，把1变成0
                        total -= nums[i]
                        win[state] = player
                        return player

                    state ^= cur  # 回溯
                    total -= nums[i]
                cur <<= 1

            return player*-1

        if desiredTotal == 0:
            return True
        if sum(range(1,maxChoosableInteger+1)) < desiredTotal:
            return False
        return winner(0, 1) == 1

print(Solution().canIWin(20, 152))