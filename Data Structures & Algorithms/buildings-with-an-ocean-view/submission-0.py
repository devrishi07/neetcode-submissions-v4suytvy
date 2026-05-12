class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for i, height in enumerate(heights):
            while stack and height >= stack[-1][1]:
                stack.pop()
            
            stack.append([i, height])
        
        res = [building[0] for building in stack]
        return res