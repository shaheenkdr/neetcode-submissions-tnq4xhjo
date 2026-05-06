class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        for i in range (len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            lx = i + 1

            rx = len(nums) - 1

            while lx < rx:

                total = nums[i] + nums[lx] + nums[rx]

                if total > 0:
                    rx-=1
                
                elif total < 0:
                    lx+=1

                else:
                    res.append([nums[i], nums[lx], nums[rx]])
                    lx+=1

                    while lx < rx and nums[lx] == nums[lx-1]:
                        lx+=1
        
        return res




        