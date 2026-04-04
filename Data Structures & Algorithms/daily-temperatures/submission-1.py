class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                result[stackInd] = index - stackInd
            stack.append([index, temp])
        
        return result
