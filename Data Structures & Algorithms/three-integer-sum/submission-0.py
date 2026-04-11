class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i, num in enumerate(nums):


            pt1, pt2 = i+1, len(nums) - 1

            while pt1 < pt2:

                if num + nums[pt1] + nums[pt2] > 0:
                    pt2-=1
                
                elif num + nums[pt1] + nums[pt2] < 0:
                    pt1+=1
                
                else:
                    res.add((num,nums[pt1],nums[pt2]))
                    pt1+=1

                    while nums[pt1] == nums[pt1-1] and pt1 < pt2:
                        pt1+=1
        
        return [list(x) for x in res]

        