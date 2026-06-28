class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1, ptr2 = 0, len(nums) - 1
        cur = 0
        while cur <= ptr2:
            if nums[cur] == 0:
                nums[ptr1], nums[cur] = nums[cur], nums[ptr1]
                ptr1 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[ptr2], nums[cur] = nums[cur], nums[ptr2]
                ptr2 -= 1
            else:
                cur += 1 