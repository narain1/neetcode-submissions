class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solved with two pointer and sorting
        n = len(nums)
        nums.sort()
        result = []

        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # skiping duplicates block
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                    

                if total > 0:
                    right -= 1

                if total < 0:
                    left += 1

        return result