from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = r = 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] += 1 

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            
            res = max(res, sum(freq.values()))

        
        return res

            

                

        
 