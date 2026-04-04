class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            count = 0
            while stack and stack[-1][1] < temp:
                i, old_temp = stack.pop()
                res[i] = idx - i
            
            stack.append([idx, temp])
        
        return res
