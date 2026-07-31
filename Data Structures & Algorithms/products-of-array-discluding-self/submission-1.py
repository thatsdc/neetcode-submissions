class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Using division operator
        total = 1
        zero_counter = 0
        for v in nums:
            if v != 0:
                total *= v
            else: 
                zero_counter += 1
                if zero_counter > 1: return [0 for i in range(len(nums))]

        if zero_counter == 1: 
            return [0 if v != 0 else total for v in nums]

        result = []
        for i, v in enumerate(nums):
            result.append(int(total/v))

        return result