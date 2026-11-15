import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        max_heap = []

        for n in nums: 
            if elements.get(n) is not None:
                elements[n] += 1
            else: 
                elements[n] = 1

        for a, b in elements.items():
            map_heap = heapq.heappush(max_heap, (-b, a))

        result = []
        c = k
        while c > 0:
            _ , v = heapq.heappop(max_heap)
            result.append(v)
            c -= 1

        return result