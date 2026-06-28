class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        l = len(nums)
        res = set()

        for n in nums:
            d[n] += 1
            if d[n] > l / 3:
                res.add(n)
        return list(res) 
