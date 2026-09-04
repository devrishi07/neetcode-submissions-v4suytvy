class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def is_valid(size: int) -> bool:
            splits = 1
            sub_sum = 0
            
            for num in nums:
                sub_sum += num
                if sub_sum > size:
                    splits += 1
                    if splits > k:
                        return False
                    sub_sum = num
            
            return True

        while l < r:
            mid = (l + r) // 2

            if is_valid(mid):
                r = mid
             
            else:
                l = mid + 1
        
        return l
        


                
