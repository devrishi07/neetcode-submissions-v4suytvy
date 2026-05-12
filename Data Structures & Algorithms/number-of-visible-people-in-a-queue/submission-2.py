class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n


        for i in range(1, n):
            x = -1
            temp = i
            j = i
            while j:
                if heights[j - 1] > x:
                    res[j - 1] += 1
                    x = heights[j - 1]
                if x > heights[temp]:
                    break
                j -= 1
        
        return res



                

