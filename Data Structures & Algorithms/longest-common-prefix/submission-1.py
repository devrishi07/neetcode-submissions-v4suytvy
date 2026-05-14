class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word1 = max(strs)
        word2 = min(strs)
        common = 0

        for i in range(len(word2)):
            if word1[i] != word2[i]:
                return word2[:i]
        
        return word2
        
