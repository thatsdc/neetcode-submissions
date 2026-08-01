class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Algorithm has to be O(n) so we can't order the list 

        num_set = set(nums)
        lengths = {}
        max_len = 0

        for n in num_set:
            # Find the length of the left and right adjacent sequences
            left = lengths.get(n - 1, 0)
            right = lengths.get(n + 1, 0)

            # The total length of the new joined sequence
            current_len = left + right + 1
            max_len = max(max_len, current_len)

            # Update the number itself and the limits (the "terminals") of the sequence
            lengths[n] = current_len
            lengths[n - left] = current_len
            lengths[n + right] = current_len

        return max_len
        