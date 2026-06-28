class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        acc = [i * -1 for i in stones]
        heapq.heapify(acc)
        while len(acc) > 1:
            a = heapq.heappop(acc)
            b = heapq.heappop(acc)
            if b > a:
                heapq.heappush(acc, a - b)
        print(acc)
        acc.append(0)
        return abs(acc[0])