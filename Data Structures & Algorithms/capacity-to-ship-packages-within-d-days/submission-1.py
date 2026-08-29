class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canDo(cap):
            no_days, currCap = 1, cap

            for w in weights:
                if currCap - w < 0:
                    no_days += 1
                    if no_days > days:
                        return False
                    currCap = cap

                currCap -= w
            return True
        
        while l <= r:
            mid = (l + r) // 2

            if canDo(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1





        
        return res


