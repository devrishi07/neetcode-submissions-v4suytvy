from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        answer = []

        for string in strs:
            sorted_word = "".join(sorted(string))
            
            hashmap[sorted_word].append(string)
        
        return list(hashmap.values())