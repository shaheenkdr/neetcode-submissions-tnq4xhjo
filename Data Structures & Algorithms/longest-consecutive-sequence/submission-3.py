class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        data = set(nums)
        largest = 0 

        if len(nums) == 1:
            return 1


        for num in nums:

            if num in data:
                large=1

                while num+1 in data: 
                    
                    num+=1
                    large+=1

                largest = max(large, largest)


        return largest                

        