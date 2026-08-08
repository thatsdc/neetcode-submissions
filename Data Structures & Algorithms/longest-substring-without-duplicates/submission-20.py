class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = dict()
        i = 0
        max_len = 0
        ph = 0

        for j in range(len(s)): 
            c = s[j]
            if c in last_seen and last_seen[c] >= i:
                i = last_seen[c]+1


            last_seen[c] = j
            
            curr_len = j - i + 1
            if curr_len > max_len:
                max_len = curr_len
            
        return max_len
