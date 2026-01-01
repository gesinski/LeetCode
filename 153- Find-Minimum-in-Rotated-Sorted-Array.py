class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while nums[l] > nums[r]:
            l += 1
            if nums[r] > nums[r-1]:
                r -= 1
            else: 
                return nums [r]
        return nums[l]