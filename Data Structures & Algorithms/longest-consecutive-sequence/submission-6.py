class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0


        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                streak = 1

                while current + 1 in nums_set:
                    streak += 1
                    current += 1

                longest_streak = max(streak, longest_streak)

        return longest_streak