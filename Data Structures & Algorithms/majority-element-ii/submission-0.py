from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        k = len(nums) // 3 

        res = []
        for count in counts:
            if counts[count] > k:
                res.append(count)
        
        return res


        