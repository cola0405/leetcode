class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l,r = '',''
        for c in moves:
            if c != '_':
                l += c
                r += c
            else:
                l += 'L'
                r += 'R'

        d1 = l.count('L') - l.count('R')
        d2 = r.count('R') - r.count('L')
        return max(d1,d2)

