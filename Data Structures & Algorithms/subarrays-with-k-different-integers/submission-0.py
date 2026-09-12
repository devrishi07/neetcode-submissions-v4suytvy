from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atleastk(k: int) -> int:
            seen = defaultdict(int)
            unique = 0
            l = 0
            res = 0
            n = len(nums)

            for r in range(n):
                
                if nums[r] not in seen:
                    unique += 1

                seen[nums[r]] += 1
                
                while unique >= k:
                    res +=  n - r
                    seen[nums[l]] -= 1

                    if seen[nums[l]] == 0:
                        seen.pop(nums[l])
                        unique -= 1
                    
                    l += 1
            return res

        return atleastk(k) - atleastk(k + 1)
                


                    





