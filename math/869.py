class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        table = []
        num = 1
        while num <= 1e9:
            table.append(''.join(sorted(list(str(num)), reverse=True)))
            num <<= 1
        return ''.join(sorted(list(str(n)), reverse=True)) in table

print(Solution().reorderedPowerOf2())