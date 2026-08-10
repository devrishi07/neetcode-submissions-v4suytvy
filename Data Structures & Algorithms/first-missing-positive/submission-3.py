class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)                 
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
            
        for i in range(n):
            if abs(nums[i]) > 0 and abs(nums[i]) <= n:
                x = abs(nums[i]) - 1
                if nums[x] != 0:
                    nums[x] = nums[x] * -1 if nums[x] > 0 else nums[x]
                else:
                    nums[x] = -(n + 1)

        for i in range(1, n + 1):
            if not nums[i - 1] < 0:
                return i
        
        return n + 1
        


