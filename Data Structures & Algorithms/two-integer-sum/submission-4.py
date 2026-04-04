class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            composite = target - nums[i] 
        
            if composite in hashmap:
                return [hashmap[composite], i]
            
            hashmap[nums[i]] = i
    




