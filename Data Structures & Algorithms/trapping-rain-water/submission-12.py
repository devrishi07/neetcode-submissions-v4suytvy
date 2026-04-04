class Solution:
    def trap(self, height: List[int]) -> int:
      n = len(height)  
      trapped_water = 0

      left_max_array = [0] * n
      left_max = 0

      for i in range(n):
        left_max_array[i] = left_max
        left_max = max(left_max, height[i])
      
      right_max_array = [0] * n
      right_max = 0

      for i in range(n-1, -1, -1):
        right_max_array[i] = right_max
        right_max = max(right_max, height[i])
      
      for i in range(n):
        water = min(left_max_array[i], right_max_array[i]) - height[i] 
        trapped_water += water if water > 0 else 0
      
      return trapped_water




