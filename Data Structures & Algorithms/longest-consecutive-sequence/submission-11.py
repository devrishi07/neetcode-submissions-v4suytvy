class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_streak = 0

        for num in seen:
            if num - 1 not in seen:
                current = num
                streak = 1

                while current + 1 in seen:
                    streak += 1
                    current += 1

                longest_streak = max(longest_streak, streak)
        
        return longest_streak