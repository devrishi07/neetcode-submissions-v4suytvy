class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0


        for num in nums:
            if num-1 not in nums:
                streak = 1
                current = num

                while current + 1 in nums:
                    streak += 1
                    current += 1
                
                longest_streak = max(longest_streak, streak)
        
        return longest_streak