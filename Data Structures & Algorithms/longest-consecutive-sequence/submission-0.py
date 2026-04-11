class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)

        l1 = 0

        for num in nums:

            l2 = 0

            if num - 1 not in seen:

                while num+l2 in seen:
                    l2+=1
            

            l1 = max(l1,l2)
        
        return l1



