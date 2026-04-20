class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)

        lcs = 0

        for num in nums:

            if num - 1 in seen:
                continue
            
            count = 1
            while (num + 1) in seen:
                count+=1
                num+=1
            
            lcs = max(lcs, count)
        
        return lcs

        