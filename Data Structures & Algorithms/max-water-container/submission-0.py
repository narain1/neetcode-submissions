class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                max_v = max(min(heights[i], heights[j]) * (j-i), max_v)
        return max_v