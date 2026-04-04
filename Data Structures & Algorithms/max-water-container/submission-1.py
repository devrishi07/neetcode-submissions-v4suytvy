class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area,left = 0, 0, 
        right = len(heights) - 1

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(area, max_area)

            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        
        return max_area

