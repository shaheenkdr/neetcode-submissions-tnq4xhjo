import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}

        heap = []

        for num in nums:

            if num in hmap:
                hmap[num]+=1
            
            else:
                hmap[num] = 1
        

        for key,value in hmap.items():
            heapq.heappush(heap,(-value,key))

        res = []
        for i in range(k):
            _,val = heapq.heappop(heap)
            res.append(val)
        

        return res


