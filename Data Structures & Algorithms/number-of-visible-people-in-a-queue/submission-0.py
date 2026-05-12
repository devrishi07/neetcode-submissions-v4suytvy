class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n


        for i in range(1, n):
            x = -1
            temp = i
            while i:
                if heights[i - 1] > x:
                    res[i - 1] += 1
                x = max(heights[i - 1], x)
                if x > heights[temp]:
                    break
                i -= 1
        
        return res



                

