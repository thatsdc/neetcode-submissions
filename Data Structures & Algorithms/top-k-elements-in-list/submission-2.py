class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for n in nums: 
            frequency[n] = frequency.get(n, 0) + 1

        for n, c in frequency.items():
            buckets[c].append(n)
 
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res