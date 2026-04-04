class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        right_smaller = [0] * n 
        stack = []

        # Compute the distance to the nearest smaller to the right
        for idx in range(n):
            
            while stack and heights[idx] < stack[-1][1]:
                i, temp = stack.pop()
                right_smaller[i] = idx - i
            
            stack.append((idx, heights[idx]))
        
        for idx, height in stack:
            right_smaller[idx] = n - idx


        left_smaller = [0] * n 
        stack = []

        for idx in range(n - 1, -1, -1):
            
            while stack and heights[idx] < stack[-1][1]:
                i, temp = stack.pop()
                left_smaller[i] = i - idx
            
            stack.append((idx, heights[idx]))
        
        for idx, height in stack:
            left_smaller[idx] = idx + 1

        max_area = 0 
        for i in range(n):
            area = heights[i] * (left_smaller[i] + right_smaller[i] - 1)
            max_area = max(area, max_area)
        
        return max_area










        

        