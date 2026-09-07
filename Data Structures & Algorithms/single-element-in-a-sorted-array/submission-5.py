class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1: return nums[0]

        while l <= r:
            mid = (l + r) // 2

            if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                if (mid - 1 - l) % 2 == 0:
                    l = mid + 1
                else:
                    r = mid - 2

            elif mid + 1 < n and nums[mid + 1] == nums[mid]:
                if (r - (mid + 1)) % 2 == 0:
                    r = mid - 1
                else: 
                    l = mid + 2
            else:
                return nums[mid]