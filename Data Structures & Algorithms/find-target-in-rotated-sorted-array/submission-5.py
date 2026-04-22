class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lx , rx = 0 , len(nums) - 1 

        while lx <= rx:

            mid = (lx + rx) // 2

            if nums[mid] == target:
                return mid

            if nums[lx] <= nums[mid]:

                if nums[lx] <= target < nums[mid]:
                    rx = mid - 1
                else:
                    lx = mid + 1
            
            else:
                if nums[mid] < target <= nums[rx]:
                    lx = mid + 1 
                else:
                    rx = mid - 1
        
        return -1
        