from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        fmap = Counter(nums)

        heap = []
        res = []

        for num, count in fmap.items():
            heapq.heappush(heap, (-count, num))

        
        for i in range(k):
            _, val = heapq.heappop(heap)
            res.append(val)
        
        return res



        