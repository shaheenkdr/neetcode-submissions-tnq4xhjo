class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        seen = {}

        for num in nums:

            seen[num] = seen.get(num, 0) + 1 
        

        for num, freq in seen.items():

            if freq > len(nums) // 2: 
                return num
        