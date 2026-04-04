class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1

        while left < right:
            two_sum = numbers[right] + numbers[left]

            if two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                return [index + 1 for index in (left, right)]
        