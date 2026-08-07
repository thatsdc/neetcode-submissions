class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a_idx = 0
        b_idx = len(heights) - 1
        max_amount = 0

        while a_idx < b_idx: 
            curr_amount = min(heights[a_idx], heights[b_idx]) * (b_idx - a_idx)

            if curr_amount > max_amount:
                max_amount = curr_amount

            if heights[a_idx] < heights[b_idx]:
                a_idx += 1
            else: 
                b_idx -= 1

        return max_amount
        