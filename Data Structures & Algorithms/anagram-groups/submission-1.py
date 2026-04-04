class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        answer = []

        for string in strs:
            sorted_word = "".join(sorted(string))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = []
            
            hashmap[sorted_word].append(string)
        
        for group in hashmap.values():
            answer.append(group)
        
        return answer