from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        res = max_count = 0

        for num in nums:
            hashmap[num] += 1
            if max_count < hashmap[num]:
                max_count = hashmap[num]
                res = num
                if max_count > len(nums) // 2: return res
        




        