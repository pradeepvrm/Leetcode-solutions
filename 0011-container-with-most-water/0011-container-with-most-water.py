class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            side = min(height[left], height[right])
            curr_area = side * (right - left)
            area = max(area, curr_area)

            if height[left] <= height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1
        return area