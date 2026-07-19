class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        hashmap = {0 : 1}

        for num in nums:
            prefix += num
            if prefix - k in hashmap:
                count += hashmap[prefix - k]
            hashmap[prefix] = hashmap.get(prefix, 0) + 1
        
        return count



        