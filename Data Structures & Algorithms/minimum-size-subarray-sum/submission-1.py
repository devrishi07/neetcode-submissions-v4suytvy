class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        current = 0
        l = 0

        for r in range(len(nums)):
            current += nums[r]

            while current >= target:
                min_len = min(min_len, r - l + 1)
                current -= nums[l]
                l += 1


        return 0 if min_len == float("inf") else min_len
            

