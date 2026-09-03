import math 
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = math.ceil(x / 2)

        while l < r:
            m = math.ceil((l + r) /2)

            if m * m > x:
                r = m - 1

            elif m * m < x:
                l = m

            else:
                return m
        
        return l
            


            

