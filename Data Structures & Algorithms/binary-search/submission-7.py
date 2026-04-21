class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lx, rx = 0, len(nums) - 1

        while lx <= rx: 
            mid = (lx + rx) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                lx = mid + 1
            else:
                rx = mid - 1
        
        return -1
        