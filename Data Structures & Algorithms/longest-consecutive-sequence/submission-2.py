class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Algorithm has to be O(n) so we can't order the list 
        prev = {}

        # Fill the dict
        for n in nums: 
            if prev.get(n-1) is not None:
                prev[n] = n - 1
            else:
                prev[n] = n

            if prev.get(n+1) is not None:
                prev[n+1] = n

        # Iterate and get only keys with None value
        starters = []
        for k, v in prev.items():
            if k == v: 
                starters.append(k)
                
        # Backtrack and compose all the sequences starting from None value
        seq_max = 0
        for s in starters:
            c = 0
            v = s

            while v is not None: 
                c += 1
                v = prev.get(s+c)
            
            if c > seq_max: seq_max = c

        return seq_max
        