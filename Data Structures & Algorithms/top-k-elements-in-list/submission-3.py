class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        q = []
        for n, v in count.items():
            heapq.heappush(q, (v, n))
            if len(q) > k:
                heapq.heappop(q)
        return [j for i, j in q]
