class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        Maxarea = 0

        for i in range(len(heights)):
            current = heights[i]
            rightMost = i + 1

            while rightMost < n and heights[rightMost] >= current:
                rightMost += 1
            
            leftMost = i - 1

            while leftMost > -1 and heights[leftMost] >= current:
                leftMost -= 1
            
            Maxarea = max(Maxarea, current * (rightMost - leftMost - 1)) 
        
        return Maxarea