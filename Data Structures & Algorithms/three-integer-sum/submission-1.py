class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        n = len(nums)

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            lx = i+1
            rx = n - 1

            while lx < rx :

                temp = nums[i] + nums[lx] + nums[rx]

                if temp < 0 :
                    lx+=1
                
                elif temp > 0:
                    rx-=1
                
                else:
                    res.append([nums[i], nums[lx], nums[rx]])
                    lx+=1

                    while nums[lx] == nums[lx-1] and lx < rx:
                        lx+=1
        
        return res


        