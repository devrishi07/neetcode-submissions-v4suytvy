class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        right_smaller = [0] * n 
        stack = []

        # Compute the distance to the nearest smaller to the right
        for idx, height in enumerate(heights):
            
            while stack and height < stack[-1][1]:
                i, temp = stack.pop()
                right_smaller[i] = idx - i
            
            stack.append((idx, height))
        
        for idx, height in stack:
            right_smaller[idx] = n - idx


        left_smaller = [0] * n 
        stack = []

        for idx, height in zip(range(n - 1, -1, -1), reversed(heights)):
            
            while stack and height < stack[-1][1]:
                i, temp = stack.pop()
                left_smaller[i] = i - idx
            
            stack.append((idx, height))
        
        for idx, height in stack:
            left_smaller[idx] = idx + 1

        max_area = 0 
        for h, l, r in zip(heights, left_smaller, right_smaller):
            area = h * (l + r - 1)
            max_area = max(area, max_area)
        
        return max_area










        

        