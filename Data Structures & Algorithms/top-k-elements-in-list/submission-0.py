import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        heap = []

        for num in nums:

            if num in seen:
                seen[num]+=1
            else:
                seen[num] = 1 
        

        for num, freq in seen.items():
            heapq.heappush(heap, (-freq,num))
        
        res = []

        for _ in range(k):
            _,val = heapq.heappop(heap)
            res.append(val)
        
        return res


