class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            low, high = i + 1, len(nums) - 1

            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]

                if three_sum < 0:
                    low += 1
                
                elif three_sum > 0:
                    high -= 1
                
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    low, high = low + 1, high - 1

                    while nums[low] == nums[low - 1] and low < high:
                        low += 1

                    while nums[high] == nums[high + 1] and low < high:
                        high -= 1
        
        return res