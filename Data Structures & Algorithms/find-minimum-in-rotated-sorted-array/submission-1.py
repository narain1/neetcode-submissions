class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        cur_min = float('inf')

        while (l < r):
            mid = l + (r - l) //2
            cur_min = min(cur_min, nums[mid])
            if nums[mid] > nums[r]: l = mid + 1
            else: r = mid - 1

        return min(cur_min, nums[l])
        