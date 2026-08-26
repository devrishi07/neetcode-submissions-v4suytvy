from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = Counter(nums)

        buckets = [[] for ashish in range(n + 1)]

        for elem, freq in counts.items():
            buckets[freq].append(elem)
        

        res = []
        for i in range(n, -1, -1):
            if buckets[i]:
                res.extend(buckets[i])
                if len(res) >= k:
                    return res[:k]
        
        return res
    





        