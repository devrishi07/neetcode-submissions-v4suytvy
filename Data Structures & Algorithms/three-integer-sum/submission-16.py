from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                current_sum = nums[l] + nums[r]
                
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    # Append the actual values, not the indices
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # Move pointers and skip duplicates for l and r
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                    
        return res
