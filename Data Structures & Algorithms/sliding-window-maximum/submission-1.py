class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        deq = collections.deque() # store indices

        lx = rx = 0

        while rx < len(nums):

            while deq and nums[deq[-1]] < nums[rx]:
                deq.pop()
            
            deq.append(rx)

            if deq[0] < lx:
                deq.popleft()
            
            if (rx - lx + 1) >= k:
                res.append(nums[deq[0]])
                lx +=1
            
            rx+=1
        
        return res


        