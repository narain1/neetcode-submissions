class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        # freq = [(v, K) for K, v in count.items()]
        # freq = sorted(freq, key=lambda x: x[0], reverse=True)
        # return [x[1] for x in freq[:k]]

        heap = []
        for K, v in count.items():
            heapq.heappush(heap, (-v, K))

        return [heapq.heappop(heap)[1] for i in range(k)]

        