class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):
                two_sum = nums[i] + nums[j]

                if two_sum == target:
                    return [i, j]






