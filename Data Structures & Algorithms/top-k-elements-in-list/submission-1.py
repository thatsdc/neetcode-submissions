class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        
        for n in nums: 
            if frequency.get(n) is not None: 
                frequency[n] += 1
            else: 
                frequency[n] = 1
        
        return [el[0] for el in sorted(list(frequency.items()), key=lambda x: x[1], reverse=True)[:k]]