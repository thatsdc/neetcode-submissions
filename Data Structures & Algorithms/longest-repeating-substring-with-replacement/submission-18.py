class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        i = 0
        max_len = 0
        max_freq = 0
        for j in range(len(s)):
            c = s[j]
            
            freq[c] = freq.get(c, 0) + 1

            max_freq = max(max_freq, freq[c])
            if (j - i + 1) - max_freq > k: 
                i += 1
                freq[s[i-1]] -= 1

            max_len = max(max_len, j - i + 1)
            
        return max_len
