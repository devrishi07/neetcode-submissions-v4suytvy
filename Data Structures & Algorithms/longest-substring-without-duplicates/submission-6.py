class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left = res = 0

        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            
            unique.add(s[right])
            res = max(right - left + 1, res)
        
        return res



            
            

                

            

        