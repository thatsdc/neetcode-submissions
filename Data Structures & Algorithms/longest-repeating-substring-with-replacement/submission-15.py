class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        i = 0
        max_len = 0
        for j in range(len(s)):
            c = s[j]
            
            if c not in freq:
                freq[c] = 1
            else: 
                freq[c] += 1

            highest_item = max(freq.items(), key=lambda item: item[1])
            while (j - i + 1) - highest_item[1] > k and i < j: 
                i += 1
                freq[s[i-1]] -= 1

            max_len = max(max_len, j - i + 1)
            
        return max_len
