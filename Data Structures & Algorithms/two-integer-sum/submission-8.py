class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            semax = target - nums[i]

            if semax in hashmap:
                return [hashmap[semax], i]
            
            hashmap[nums[i]] = i



