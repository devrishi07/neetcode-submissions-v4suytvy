class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        max_len = 0

        for char in s:
            while char in stack:
                stack.pop(0)
            
            stack.append(char)
            
            max_len = max(len(stack), max_len)
        
        return max_len
