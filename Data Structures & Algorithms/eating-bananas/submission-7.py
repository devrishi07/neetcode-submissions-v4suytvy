import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r
        
        while l <= r:
            k = (r + l) // 2
            t = 0
            for pile in piles:
                t += math.ceil(pile / k)

            if t > h:
                l = k + 1
            elif t <= h:
                r = k - 1
                best = min(best, k)
        
        return best
            
