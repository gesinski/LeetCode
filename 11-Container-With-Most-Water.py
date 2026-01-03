class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0

        l, r = 0, len(height) -1 
        while l < r:
            currArea = (r-l) * min(height[l], height[r])
            result = max(result, currArea)

            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            elif l + 1 < r - 1:
                if height[l+1] > height[r-1]:
                    r -= 1
                else:
                    l += 1
            else:
                break

        return result 