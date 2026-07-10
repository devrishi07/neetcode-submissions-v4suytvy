from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        counts = Counter(nums)

        for num, freq in counts.items():
            buckets[freq].append(num)

        answer = []
        for i in range(n, -1, -1):
            if buckets[i]:
                answer.extend(buckets[i])
                if len(answer) >= k:
                    return answer


        









