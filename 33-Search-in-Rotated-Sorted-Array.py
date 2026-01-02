class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)//2
        r = len(nums)-1

        if nums[m] == target:
            return m
        
        if (nums[m] < target and nums[r] >= target):
            p = m
        else:
            p = 0
        for i in range(p, len(nums)):
            if nums[i] == target:
                return i
            if nums[r] == target:
                return r
            r -= 1
            
        return -1