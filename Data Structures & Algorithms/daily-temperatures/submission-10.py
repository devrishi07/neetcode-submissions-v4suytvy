class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > stack[-1][1]:
                idx, t = stack.pop()
                res[idx] = i - idx
            
            stack.append((i, temperatures[i]))
        return res